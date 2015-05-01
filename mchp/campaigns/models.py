from django.core.mail import get_connection, EmailMultiAlternatives
from django.db import models
from django.template import Context, Template
from django.utils import timezone
from django.utils.html import strip_tags

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
        The `recipient` dict must contain at minimum `subject`, `body`, and
        `email` keys.

        """
        print(connection)
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
        recipients : list or tuple of dicts
            A list or tuple of dicts representing recipients.

        Returns
        -------
        num_sent : int
            The count of messages sent.

        """
        connection = get_connection()
        connection.open()

        num_sent = 0
        for recipient in recipients:
            self._send_message(recipient, connection)
            num_sent += 1

        connection.close()

        return num_sent

    def send(self):
        if self.active:
            recipients = [{'name':'andrew','email':'hey@yo.com', 'body':'why'}]
            num_sent = self._send_messages(recipients)
            print('Successfully sent {} message(s)'.format(num_sent))
        else:
            raise RuntimeError("Not active")

    class Meta:
        abstract = True


class CampaignMailer(BaseCampaignMailer):
    """ A concrete campaign class.

    Attributes
    ----------
    title : django.db.models.CharField
        An internal name to identify this campaign.

    """
    title = models.CharField(max_length=255)

    def str(self):
        pass
