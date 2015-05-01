from django.core.mail import EmailMessage
from django.db import models
from django.utils import timezone


class BaseCampaign(models.Model):
    """ Abstract base class for campaigns.

    Attributes
    ----------
    subject : django.db.models.CharField
        A subject for the campaign.
    body : django.db.models.TextField
        A body for the message.
    sent : django.db.models.DateTimeField, optional
        When the campaign was sent, or `None` otherwise.

    """
    # recipients = models.ManyToManyField()
    subject = models.CharField(max_length=78)
    body = models.TextField()
    sent = models.DateTimeField(blank=True, null=True)

    def _send_campaign(self):
        """ Build a campaign.

        Returns
        -------
        campaign : django.core.mail.EmailMessage
            A message, ready to send.

        """
        return 0
        # campaign = EmailMessage(subject, body, from, [to])
        # return campaign

    def send(self):
        if not self.sent:
            num_sent = self._send_campaign()
            print('Successfully sent {} message(s)'.format(num_sent))
            self.sent = timezone.now()
            self.save(update_fields=['sent'])
        else:
            raise RuntimeError("Already sent: {}".format(self.sent))

    class Meta:
        abstract = True


class Campaign(BaseCampaign):
    """ A concrete campaign class.

    Attributes
    ----------
    title : django.db.models.CharField
        An internal name to identify this campaign.

    """
    title = models.CharField(max_length=255)

    def str(self):
        pass
