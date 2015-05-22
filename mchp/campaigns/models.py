from django.core.mail import get_connection
from django.db import models
from django.template import Context, Template
from django.utils import timezone
from django.conf import settings
from . import managers

import smtplib
from . import utils


class BaseCampaignSubscriber(models.Model):
    """ Abstract base class for subscriber in a campaign.

    Attributes
    ----------
    uuid : django.db.models.CharField
        A universally-unique identifier for the user.
    notified : django.db.models.DateTimeField, optional
        When was this user notified?
    clicked : django.db.models.DateTimeField, optional
        When did this user first click through the e-mail?
    opened : django.db.models.DateTimeField, optional
        When did this user first open the e-mail?
    unsubscribed : django.db.models.DateTimeField, optional
        When did this user first unsubscribe from the e-mail?

    """
    uuid = models.CharField(max_length=32, unique=True,
                            default=utils.make_uuid)
    notified = models.DateTimeField(blank=True, null=True)
    clicked = models.DateTimeField(blank=True, null=True)
    opened = models.DateTimeField(blank=True, null=True)
    unsubscribed = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def mark_notified(self):
        """ Mark subscriber as notified now. """
        self.notified = timezone.now()
        self.save(update_fields=['notified'])


class CampaignSubscriber(BaseCampaignSubscriber):
    """ Subscriber in a campaign.

    Attributes
    ----------
    user : django.db.models.ForeignKey
        A user account backing this subscriber.
    campaign : django.db.models.ForeignKey
        The campaign associated with this subscriber.

    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    campaign = models.ForeignKey('Campaign', related_name='subscribers')
    objects = managers.SubscriberManager()

    class Meta:
        unique_together = ('campaign', 'user')

    def __str__(self):
        return self.user.get_full_name()


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
    body = models.TextField(blank=True)

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
    slug = models.SlugField(max_length=255, unique=True,
        help_text='Used by the campaign automailer.  Change with caution!')  # noqa

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{} ({})'.format(self.name, self.slug)

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
    """ A metaclass for an e-mail campaign.

    Attributes
    ----------
    when : django.db.models.DateTimeField, optional
        When does this campaign start?
    until : django.db.models.DateTimeField
        When does this campaign end?

    Notes
    -----
    A campaign is considered inactive if `when` is unset or in the future
    or if `until` is past.

    """
    when = models.DateTimeField("campaign start")
    until = models.DateTimeField("campaign end", blank=True, null=True)

    class Meta:
        abstract = True

    def active(self):
        """ Is this campaign active?

        Returns
        -------
        out : bool
            `True` if this campaign is active, `False` otherwise.

        """
        if self.when <= timezone.now():
            if not self.until or self.until >= timezone.now():
                return True
        return False
    active.boolean = True

    def blast(self, force=False, context=None):
        """ Send a blast to this campaign.

        Parameters
        ----------
        force : bool, optional
            `True` to notify subscribers who have already been notified,
            `False` otherwise.  Default `False`.
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """
        if self.active():
            self._blast(force=force, context=context)

    def clicked(self):
        """ How many subscribers have clicked through their messages? """
        return self.subscribers.objects.exclude(clicked=None).count()

    def opened(self):
        """ How many subscribers have opened their messages? """
        return self.subscribers.objects.exclude(opened=None).count()

    def unsubscribed(self):
        """ How many subscribers have unsubscribed from their messages? """
        return self.subscribers.objects.exclude(unsubscribed=None).count()

    def _blast(self, context=None, force=False):
        """ Send a blast to this campaign if it is active.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.
        force : bool, optional
            `True` to notify subscribers who have already been notified,
            `False` otherwise.  Default `False`.
            [TODO] remove this arg?

        """
        recipients = self.subscribers.all()  # filter(unsubscribed=None)
        if not force:
            recipients = recipients.filter(notified__isnull=True)
        if recipients:
            connection = get_connection()
            connection.open()
            for recipient in recipients:
                msg_context = context.copy() if context else {}
                msg_context.update(recipient=recipient)
                message = self._message(recipient.user.email,
                                        connection,
                                        msg_context)
                try:
                    message.send()
                except smtplib.SMTPException:
                    raise
                else:
                    recipient.mark_notified()
            connection.close()


class Campaign(BaseCampaign):
    """ Concrete campaign class.

    Attributes
    ----------
    name : django.db.models.CharField
        An internal name to identify this campaign.
    template : django.db.models.ForeignKey
        A template associated with this campaign.
    sender : django.db.models.EmailField
        An e-mail address for the sender.
    sender_name : django.db.models.CharField, optional
        A name for the sender.  Will be escaped as necessary.
    objects : django.db.models.Manager
        A model manager for this class.

    """
    name = models.CharField(max_length=255)
    template = models.ForeignKey(CampaignTemplate)
    sender = models.EmailField(max_length=254)
    sender_name = models.CharField(max_length=254, blank=True)
    objects = managers.CampaignManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def _message(self, recipient, connection, context=None):
        """ Build and send a single message from a campaign.

        Parameters
        ----------
        recipient : str
            An e-mail address (and optional name) to which to send.
        connection : django.core.mail.backends.console.EmailBackend
            A connection with which to send the message.
        context : dict, optional
            A dictionary to turn into context variables for the message.

        """
        context = Context(context)

        subject = self.template.subject_template.render(context)
        body = self.template.body_template.render(context)

        return utils.make_email_message(subject, body,
                                        utils.make_display_email(
                                            self.sender,
                                            self.sender_name),
                                        recipient, connection)
