from django.core.mail import get_connection, EmailMultiAlternatives
from django.db import models
from django.template import Context, Template
from django.utils import timezone
from django.utils.html import strip_tags

from user_profile.models import Student
from . import utils

# all campaigns will be sent from this email address
CAMPAIGN_FROM_EMAIL = 'mchp <study@mycollegehomepage.com>'


class CampaignTemplate(models.Model):
    """ Contents of campaign templates.

    Attributes
    ----------
    title : django.db.models.CharField
        An internal name to identify this campaign.
    subject : django.db.models.CharField
        A subject for the campaign.
    body : django.db.models.TextField
        A template for the message.
    # last updated, created

    """
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=78)
    body = models.TextField()

    def __str__(self):
        return self.title

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


class Campaign(models.Model):
    """ A campaign tracking clicks, etc.

    """
    template = models.ForeignKey(CampaignTemplate)
    recipients = models.ManyToManyField(Student)
    # stats
    clicks = models.PositiveIntegerField(default=0)
    unsubscribes = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NewsletterCampaign(Campaign):
    """

    """
    pass


class EventCampaign(Campaign):
    """

    """
    pass


class CampaignMailer(models.Model):
    """ A mailer base class.

    Attributes
    ----------
    active : django.db.models.BooleanField
        Whether this campaign can be sent.
    template : campaigns.CampaignTemplate
        A template associated with this campaign.

    """
    EVENT_LEAD = 'EV'
    NEWSLETTER = 'NL'
    CATEGORY_CHOICES = (
        (EVENT_LEAD, 'Lead time for event'),
        (NEWSLETTER, 'Newsletter'),
    )

    # active = models.BooleanField(default=False)
    template = models.ForeignKey(CampaignTemplate)
    category = models.CharField(max_length=2,
                                choices=CATEGORY_CHOICES)
    when = models.DateTimeField("campaign start", blank=True, null=True,
        help_text='If field is unset, this mailer will be disabled.')  # noqa
    until = models.DateTimeField("campaign end", blank=True, null=True)

    # campaigns = models.ManyToManyField(Campaign)

    def __str__(self):
        return self.template.title

    def active(self):
        if self.when and self.when <= timezone.now():
            if not self.until or self.until >= timezone.now():
                return True
        return False
    active.boolean = True

    def _recipients(self):
        """ Return recipients.

        """
        # [TODO] switch statements are evil
        recipients = []
        if self.category == self.EVENT_LEAD:
            subscribers = utils.upcoming_event_subscribers()
            for subscriber in subscribers:
                recipient = {
                    # [TODO] is `email` the right field?
                    'email': subscriber.user.email,
                    'first_name': subscriber.user.first_name,
                    'last_name': subscriber.user.last_name,
                }
                recipients.append(recipient)
        return recipients

    def _send_message(self, recipient, connection):
        """ Build and send a single message from a campaign.

        Parameters
        ----------
        recipient : dict
            A recipient.
        connection : django.core.mail.backends.console.EmailBackend
            A connection with which to send the message.

        Notes
        -----
        The `recipient` dict must contain at minimum an `email` key.

        """
        context = Context(recipient)
        subject = self.template.subject_template.render(context)
        body = self.template.body_template.render(context)
        to_email = recipient['email']
        msg = EmailMultiAlternatives(subject, strip_tags(body),
                                     CAMPAIGN_FROM_EMAIL, [to_email],
                                     connection=connection)
        msg.attach_alternative(body, "text/html")
        msg.send()

    def _send_messages(self, recipients):
        """ Build and send a campaign.

        Parameters
        ----------
        recipients : list or tuple of dicts, optional
            A list or tuple of dicts representing recipients.  Default `None`.

        Returns
        -------
        num_sent : int
            The count of messages sent.

        """
        num_sent = 0
        if recipients:
            connection = get_connection()
            connection.open()

            for recipient in recipients:
                self._send_message(recipient, connection)
                num_sent += 1

            connection.close()

        return num_sent

    def send(self):
        """ Build and send a campaign, then report results.

        """
        if self.active:
            print('Processing campaign "{}"'.format(self))
            recipients = self._recipients()
            # campaign = Campaign.objects.create(students=recipients)
            num_sent = self._send_messages(recipients)
            print('Successfully sent {} message(s)'.format(num_sent))
        else:
            raise RuntimeError("Campaign not active")


# class NewsletterCampaignMailer(CampaignMailer):
#     """ A concrete campaign class for newsletters.
#
#     """
#     when = models.DateTimeField('send at')
#
#     def send(self):
#         if self.when <= timezone.now():
#             super().send()
#         else:
#             print('Not yet time')
#
#     def _recipients(self):
#         """ [TODO] return every possible recipient
#
#         """
#         return super()._recipients()
#
#
# class EventCampaignMailer(CampaignMailer):
#     """ A concrete campaign class.
#
#     """
#     def _recipients(self):
#         """ Return recipients for upcoming events.
#
#         """
#         recipients = []
#         subscribers = utils.upcoming_event_subscribers()
#         for subscriber in subscribers:
#             recipient = {
#                 'email': subscriber.user.email,  # [TODO] is this right field?
#                 'first_name': subscriber.user.first_name,
#                 'last_name': subscriber.user.last_name,
#             }
#             recipients.append(recipient)
#         return recipients

