from django.core.mail import get_connection, EmailMultiAlternatives
from django.db import models
from django.template import Context, Template
from django.utils import timezone
from datetime import timedelta
from django.utils.html import strip_tags

from calendar_mchp.models import CalendarEvent
from schedule.models import Enrollment

# all campaigns will be sent from this email address
CAMPAIGN_FROM_EMAIL = 'mchp <study@mycollegehomepage.com>'


class BaseCampaignMailer(models.Model):
    """ Abstract base class for campaigns.

    Attributes
    ----------
    subject : django.db.models.CharField
        A subject for the campaign.
    body : django.db.models.TextField
        A template for the message.
    active : django.db.models.BooleanField
        Whether this campaign can be sent.

    """
    subject = models.CharField(max_length=78)
    body = models.TextField()
    active = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.refresh_template_cache()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.refresh_template_cache()

    def refresh_template_cache(self):
        """ Refresh templates in memory.

        """
        self.templates = {
            'subject': Template(self.subject),
            'body': Template(self.body),
        }

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
        subject = self.templates['subject'].render(context)
        body = self.templates['body'].render(context)
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
            print('Processing campaign {}'.format(self.title))
            recipients = self._recipients()
            num_sent = self._send_messages(recipients)
            print('Successfully sent {} message(s)'.format(num_sent))
        else:
            raise RuntimeError("Not active")

    def _recipients(self):
        """ Get recipients.

        """
        return []

    class Meta:
        abstract = True


class CampaignMailer(BaseCampaignMailer):
    """ Another abstract campaign class, this one with a title.

    Attributes
    ----------
    title : django.db.models.CharField
        An internal name to identify this campaign.

    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class NewsletterCampaignMailer(CampaignMailer):
    """ A concrete campaign class for newsletters.

    """
    when = models.DateTimeField('send at')

    def send(self):
        if self.when <= timezone.now():
            super().send()
        else:
            print('Not yet time')

    def _recipients(self):
        """ [TODO] return every possible recipient

        """
        return super()._recipients()


class EventCampaignMailer(CampaignMailer):
    """ A concrete campaign class.

    Attributes
    ----------
    lead_time : django.db.models.PositiveIntegerField
        A lead time, in hours, for mailings before events.

    """

    def _recipients_for_event(self, event):
        """ Determine recipients for an event.

        Returns
        -------
        recipients : list
            A list of dicts of prospective recipients.

        """
        enrollments = Enrollment.objects.filter(course=event.calendar.course,
                                                receive_email=True)
        recipients = []
        for enrollment in enrollments:
            recipient = {
                'email': enrollment.student.user.email,  # [TODO] right field?
                'first_name': enrollment.student.user.first_name,
                'last_name': enrollment.student.user.last_name,
            }
            recipients.append(recipient)
        return recipients

    def _events(self):
        """ Events with notifications due.

        Returns
        -------
        out : list
            A list of events.

        """
        now = timezone.now()
        events = CalendarEvent.objects.filter(start__gte=now,
                                              notify_lead__gt=0)
        return [event for event in events
                if now > event.start - timedelta(minutes=event.notify_lead)]

    def _recipients(self):
        """ Return recipients for upcoming events.

        """
        recipients = []
        for event in self._events():
            event_recipients = self._recipients_for_event(event)
            recipients.extend(event_recipients)
        return recipients
