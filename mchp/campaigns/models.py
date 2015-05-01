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

    def _send_campaign(self, recipients):
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
            context = Context(recipient)
            subject = self.templates['subject'].render(context)
            body = self.templates['body'].render(context)
            plain_text_body = strip_tags(body)
            to_email = recipient['email']
            msg = EmailMultiAlternatives(subject, plain_text_body,
                                             CAMPAIGN_FROM_EMAIL, [to_email],
                                             connection=connection)
            msg.attach_alternative(body, "text/html")
            msg.send()
            num_sent += 1

        connection.close()

        return num_sent

    def send(self):
        if self.active:
            recipients = []
            num_sent = self._send_campaign(recipients)
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
