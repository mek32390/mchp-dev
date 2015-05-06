from django.core.mail import get_connection
from django.db import models
from django.template import Context, Template
from django.utils import timezone
from django.conf import settings

import smtplib
from . import utils

# all campaigns will be sent from this email address
CAMPAIGN_FROM_EMAIL = 'mchp <study@mycollegehomepage.com>'


class CampaignSubscriber(models.Model):
    """ A subscriber in a campaign.

    Attributes
    ----------
    campaign : campaigns.models.Campaign
        The campaign associated with this subscriber.
    user : django.db.models.ForeignKey
        A user account backing this subscriber.
    notified : django.db.models.DateTimeField
        When was this user notified?
    # did_unsubscribe : django.db.models.BooleanField
    #     Has this user unsubscribed?
    opens : django.db.models.PositiveIntegerField
        How many opens has this user generated?
    clicks : django.db.models.PositiveIntegerField
        How many click-throughs has this user generated?

    """
    campaign = models.ForeignKey('Campaign', related_name='subscribers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    notified = models.DateTimeField(blank=True, null=True)
    # unsubscribed = models.BooleanField(default=True)
    opens = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('campaign', 'user')

    def __str__(self):
        return self.user.get_full_name()

    def is_notified(self):
        """ Has this user been notified?

        """
        return self.notified is not None


class BaseCampaignTemplate(models.Model):
    """ Abstract base for contents of a campaign template.

    Attributes
    ----------
    subject : django.db.models.CharField
        A subject for the campaign.
    body : django.db.models.TextField
        A template for the message.

    """
    subject = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        abstract = True


class CampaignTemplate(BaseCampaignTemplate):
    """ Contents of a campaign template.

    Attributes
    ----------
    name : django.db.models.CharField
        An internal name to identify this campaign.

    """
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'template'
        ordering = ('name',)

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


class Campaign(BaseCampaign):
    """ Concrete campaign class.

    Attributes
    ----------
    name : django.db.models.CharField
        An internal name to identify this campaign.

    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'campaign'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def opens(self):
        """ How many opens has this campaign accumulated? """
        return self.subscribers.objects.aggregate(sum=models.Sum('clicks')).sum

    def opened(self):
        """ How many subscribers have opened their messages? """
        return self.subscribers.objects.filter(opens__gt=0).count()

    def clicks(self):
        """ How many click-throughs has this campaign accumulated? """
        return self.subscribers.objects.aggregate(sum=models.Sum('clicks')).sum

    def clicked(self):
        """ How many subscribers have clicked through their messages? """
        return self.subscribers.objects.filter(clicks__gt=0).count()

    # def unsubscribes(self):
    #     """ How many unsubscribes has this campaign accumulated? """
    #     return self.subscribers.objects.aggregate(models.Sum('unsubscribes'))

    # def unsubscribed(self):
    #     """ How many subscribers have unsubscribed from their messages? """
    #     return self.subscribers.objects.filter(unsubscribes__gt=0).count()

    def blast(self, context=None, force=False):
        """ Send a blast to this campaign if it is active.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.
        force : bool, optional
            `True` to notify subscribers who have already been notified,
            `False` otherwise.  Default `False`.

        """
        if self.active():  # [TODO] should `force` override this?
            # retrieve only subscribers that are enabled users
            active_subscribers = self.subscribers.filter(user__is_active=True)

            # limit to new subscribers if `force` is `False`
            # include all subscribers if `force` is `True`
            notify_subscribers = [s for s in active_subscribers
                                  if force or not s.is_notified()]
            if notify_subscribers:
                blast = CampaignBlast.objects.create(campaign=self)
                blast.recipients.add(*notify_subscribers)
                blast.send(context=context)


class BaseCampaignBlast(models.Model):
    """ Abstract base class for campaign blast.

    Attributes
    ----------
    campaign : campaigns.models.Campaign
        The campaign associated with this blast.
    recipients : django.db.models.ManyToManyField, optional
        Recipients for this blast.
    sent : django.db.models.DateTimeField, optional
        When this blast was created.

    """
    campaign = models.ForeignKey(Campaign)
    recipients = models.ManyToManyField(CampaignSubscriber, blank=True)
    sent = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

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
        try:
            self._send(context=context)
        except smtplib.SMTPException:
            raise
        finally:
            self.sent = timezone.now()
            self.save(update_fields=['sent'])


class CampaignBlast(BaseCampaignBlast):
    """ A campaign blast: a single slew of e-mails for one or more subscribers.

    """
    class Meta:
        verbose_name = 'blast'
        ordering = ('-sent',)

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
                message = self._message(recipient, connection, context)
                try:
                    message.send()
                except smtplib.SMTPException:
                    raise
                else:
                    recipient.notified = timezone.now()
                    recipient.save(update_fields=['notified'])
            connection.close()
