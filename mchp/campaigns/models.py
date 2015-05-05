from django.core.mail import get_connection
from django.db import models
from django.template import Context, Template
from django.utils import timezone

import smtplib
from user_profile.models import Student
from . import utils

# all campaigns will be sent from this email address
CAMPAIGN_FROM_EMAIL = 'mchp <study@mycollegehomepage.com>'


class TimestampedModelMixin(models.Model):
    """

    Attributes
    ----------
    created : django.db.models.DateTimeField
        When was this model instance first created?
    updated : django.db.models.DateTimeField
        When was this model instance last updated?

    """
    created = models.DateTimeField('first created', auto_now_add=True)
    updated = models.DateTimeField('last updated', auto_now=True)

    class Meta:
        abstract = True


class BaseCampaignTemplate(models.Model):
    """ Abstract base class for contents of campaign templates.

    Attributes
    ----------
    subject : django.db.models.CharField
        A subject for the campaign.
    body : django.db.models.TextField
        A template for the message.
    # last updated, created

    """
    subject = models.CharField(max_length=78)
    body = models.TextField()

    class Meta:
        abstract = True


class CampaignTemplate(BaseCampaignTemplate, TimestampedModelMixin):
    """ Contents of campaign templates.

    Parameters
    ----------
    name : django.db.models.CharField
        An internal name to identify this campaign.

    """
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'template'

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.refresh_template_cache()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.refresh_template_cache()

    def refresh_template_cache(self):
        """ Refresh templates in memory.

        """
        self.subject_template = Template(self.subject)
        self.body_template = Template(self.body)


class BaseCampaign(models.Model):
    """ A campaign configuration.

    Attributes
    ----------
    template : campaigns.CampaignTemplate
        A template associated with this campaign.
    when : django.db.models.DateTimeField, optional
        When does this campaign start?
    until : django.db.models.DateTimeField
        When does this campaign end?

    Notes
    -----
    A campaign is considered inactive if `when` is unset or in the future
    or if `until` is past.

    """
    template = models.ForeignKey(CampaignTemplate)
    when = models.DateTimeField("campaign start", blank=True, null=True,
        help_text='If field is unset, this campaign will be disabled.')  # noqa
    until = models.DateTimeField("campaign end", blank=True, null=True)

    class Meta:
        abstract = True

    def active(self):
        if self.when and self.when <= timezone.now():
            if not self.until or self.until >= timezone.now():
                return True
        return False
    active.boolean = True


class Subscriber(models.Model):
    """ Through table to track who's notified.

    Attributes
    ----------
    subscriber : django.db.models.ForeignKey,
        A user_profile.models.Student.
    notified : django.db.models.DateTimeField
        When was this user notified?
    # did_unsubscribe : django.db.models.BooleanField
    #     Has this user unsubscribed?
    opens : django.db.models.PositiveIntegerField
        How many opens has this user generated?
    clicks : django.db.models.PositiveIntegerField
        How many click-throughs has this user generated?

    """
    student = models.ForeignKey(Student)
    campaign = models.ForeignKey('Campaign', related_name='subscriptions')
    notified = models.DateTimeField(blank=True, null=True)
    # unsubscribed = models.BooleanField(default=True)
    opens = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('student', 'campaign')

    def __str__(self):
        return self.student.user.get_full_name()

    def is_notified(self):
        """ Has this user been notified?

        """
        return self.notified is not None


class Campaign(BaseCampaign, TimestampedModelMixin):
    """ Concrete campaign class.

    name : django.db.models.CharField
        An internal name to identify this campaign.
    subscribers : django.db.models.ManyToManyField
        Students associated with this campaign.

    """
    name = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(Student,
                                         through='Subscriber',
                                         blank=True)
    # [TODO] unsubscribes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'campaign'

    def __str__(self):
        return self.name

    def blast(self, context=None):
        """ Send a blast to this campaign if it is active.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """
        if self.subscribers and self.active():
            blast = CampaignBlast.objects.create(campaign=self)
            # access the through table here via its related name
            for subscriber in self.subscriptions.all():
                if not subscriber.is_notified():
                    blast.recipients.add(subscriber)
            blast.save()
            blast.send(context=context)

    # def notified_subscribers():
    #     self.campaign_blasts...

# Campaign.objects.create(when=course.start-course.lead, until=course.start)


class BaseCampaignBlast(models.Model):
    """ Abstract base class for campaign blast.

    Attributes
    ----------
    campaign : campaigns.models.Campaign
        A campaign associated with this mailer.
    recipients : django.db.models.ManyToManyField
        Recipients for this blast.
    sent : django.db.models.DateTimeField
        When this blast was created.

    """
    campaign = models.ForeignKey(Campaign)
    recipients = models.ManyToManyField(Subscriber,
                                        related_name='blasts',
                                        blank=True)
    sent = models.DateTimeField(blank=True, null=True)

    # clicks = models.PositiveIntegerField(default=0)
    # unsubscribes = models.PositiveIntegerField(default=0)
    # notified = models.ManyToManyField(Student)
    # unsubscribed = models.ManyToManyField(Student)

    class Meta:
        abstract = True
        verbose_name = 'blast'

    def __str__(self):
        return self.campaign.name

    def _send(self, context=None):
        """ Must override.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.

        Raises
        ------
        NotImplementedError
            If this method is not overridden.

        """
        return NotImplementedError

    def send(self, context=None):
        """ Build and send a single message from a campaign.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """
        self._send(context=context)
        self.sent = timezone.now()
        self.save(update_fields=['sent'])


class CampaignBlast(BaseCampaignBlast):
    """ A campaign blast: a single slew of e-mails for one or more subscribers.

    """
    def _message(self, recipient, connection, context=None):
        """ Build and send a single message from a campaign.

        Parameters
        ----------
        recipient : dict
            A recipient.
        connection : django.core.mail.backends.console.EmailBackend
            A connection with which to send the message.
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """

        context = context.copy() if context else {}
        context.update(recipient=recipient)
        context = Context(context)

        subject = self.campaign.template.subject_template.render(context)
        body = self.campaign.template.body_template.render(context)

        to_email = recipient.user.email  # [TODO] is this the correct address?
        return utils.make_email_message(subject, body, CAMPAIGN_FROM_EMAIL,
                                        to_email, connection)

    def _send(self, context=None):
        """ Build and send a blast.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """
        recipients = self.recipients.all()
        if recipients:
            connection = get_connection()
            connection.open()
            for recipient in recipients:
                message = self._message(recipient.student, connection, context)
                try:
                    message.send()
                except smtplib.SMTPException:
                    raise
                else:
                    recipient.notified = timezone.now()
                    recipient.save(update_fields=['notified'])
            connection.close()
