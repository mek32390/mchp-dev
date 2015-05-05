from django.core.mail import get_connection, EmailMultiAlternatives
from django.db import models
from django.template import Context, Template
from django.utils import timezone
from django.utils.html import strip_tags

import smtplib
from user_profile.models import Student
from . import utils

# all campaigns will be sent from this email address
CAMPAIGN_FROM_EMAIL = 'mchp <study@mycollegehomepage.com>'


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
        verbose_name = 'template'


class CampaignTemplate(BaseCampaignTemplate):
    """ Contents of campaign templates.

    Attributes
    ----------
    name : django.db.models.CharField
        An internal name to identify this campaign.

    """
    name = models.CharField(max_length=255)

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
        verbose_name = 'campaign'

    def active(self):
        if self.when and self.when <= timezone.now():
            if not self.until or self.until >= timezone.now():
                return True
        return False
    active.boolean = True


class Campaign(BaseCampaign):
    """ Concrete campaign class.

    name : django.db.models.CharField
        An internal name to identify this campaign.
    constituents : django.db.models.ManyToManyField
        Students associated with this campaign.

    """
    name = models.CharField(max_length=255)
    constituents = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

    def _non_notified_constituents(self):
        """ Return people who need to be notified still.

        """
        all_constituents = set(self.constituents.all())
        print(all_constituents)
        notified_in_blasts = []

        # for r in self.blasts.values_list('recipients', flat=True):
        blasts = CampaignBlast.objects.filter(campaign=self)
        for r in blasts:
            notified_in_blasts.extend(r.recipients.all())

        notified_in_blasts = set(notified_in_blasts)
        print(notified_in_blasts)

        return tuple(all_constituents)
        # return tuple(all_constituents - notified_in_blasts)

    def blast(self, context=None):
        """ Send a blast to this campaign if it is active.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """
        if self.constituents and self.active():
            blast = CampaignBlast.objects.create(campaign=self)
            for recipient in self._non_notified_constituents():
                blast.recipients.add(recipient)
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
    recipients = models.ManyToManyField(Student, related_name='blasts')
    sent = models.DateTimeField(blank=True, null=True)

    # clicks = models.PositiveIntegerField(default=0)
    # unsubscribes = models.PositiveIntegerField(default=0)
    # notified = models.ManyToManyField(Student)
    # unsubscribed = models.ManyToManyField(Student)

    class Meta:
        abstract = True
        verbose_name = 'blast'

    def __str__(self):
        return self.campaign.template.name

    def _send(self, context=None):
        """ Must override.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.

        Returns
        -------
        out : bool
            `True` if sending was successful,
            `False` otherwise.

        """
        return False

    def send(self, context=None):
        """ Build and send a single message from a campaign.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """
        if self._send(context=context):
            self.sent = timezone.now()
            self.save(update_fields=['sent'])


class CampaignBlast(BaseCampaignBlast):
    """ A campaign blast: a single slew of e-mails for one or more subscribers.

    """
    def _message(self, recipient, connection, context_dict=None):
        """ Build and send a single message from a campaign.

        Parameters
        ----------
        recipient : dict
            A recipient.
        connection : django.core.mail.backends.console.EmailBackend
            A connection with which to send the message.
        context_dict : dict, optional
            A dictionary to turn into context variables for the message.

        """
        if not context_dict:
            context_dict = {}
        context_dict.update(recipient=recipient)
        context = Context(context_dict)
        subject = self.campaign.template.subject_template.render(context)
        body = self.campaign.template.body_template.render(context)
        to_email = recipient.user.email  # [TODO] is this the correct address?
        msg = EmailMultiAlternatives(subject, strip_tags(body),
                                     CAMPAIGN_FROM_EMAIL, [to_email],
                                     connection=connection)
        msg.attach_alternative(body, "text/html")
        return msg

    def _send(self, context=None):
        """ Build and send a single message from a campaign.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """
        print('Processing campaign "{}"'.format(self))
        connection = get_connection()
        messages = [self._message(recipient, connection, context)
                    for recipient in self.recipients.all()]

        if messages:
            connection.open()
            for message in messages:
                try:
                    message.send()
                except smtplib.SMTPException as e:
                    print(e)
            connection.close()
        return True
