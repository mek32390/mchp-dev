from django.db import models
from django.utils import timezone
from campaigns.models import (MetaCampaign, BaseCampaign,
                              BaseCampaignSubscriber)
from campaigns.utils import make_email_message, make_display_email
from calendar_mchp.models import CalendarEvent
from documents.models import Document
from django.template import Context, Template
from django.template.loader import get_template

from schedule.models import Enrollment
from . import utils

# [TODO] SHOULD DELETE ALL RELATED CAMPAIGNS WHEN DELETING METACAMPAIGN


class StudyGuideCampaignSubscriber(BaseCampaignSubscriber):
    """ Subscriber in a campaign.

    Attributes
    ----------
    campaign : django.db.models.ForeignKey
        The campaign associated with this subscriber.

    """
    campaign = models.ForeignKey('StudyGuideCampaign',
                                 related_name='subscribers')

    class Meta:
        unique_together = ('campaign', 'user')


class StudyGuideCampaign(BaseCampaign):
    """ Concrete campaign class.

    Attributes
    ----------
    REQUEST_TEMPLATE : str
        The HTML template to use for study guide requests.
    PUBLISH_TEMPLATE : str
        The HTML template to use for study guide announcements.
    template : django.db.models.CharField
        A template associated with this campaign.
    subject : django.db.models.CharField
        A subject line associated with this campaign.
    event : django.db.models.ForeignKey
        An event for this campaign.
    documents : django.db.models.ManyToManyField
        Documents associated with this builder.

    """
    REQUEST_TEMPLATE = 'studyguides/request_for_study_guide.html'
    PUBLISH_TEMPLATE = 'studyguides/study_guide.html'

    template = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    event = models.ForeignKey(CalendarEvent)
    documents = models.ManyToManyField(Document,
                                       related_name='+',
                                       blank=True,
                                       null=True)

    class Meta:
        ordering = ('event',)

    def __str__(self):
        return str(self.event)

    def _message(self, recipient, connection, context=None):
        """ Build and send a single message from a campaign.

        Parameters
        ----------
        recipient : str
            An e-mail address (and optional name) to which to send.
        connection : django.core.mail.backends.console.EmailBackend
            A connection with which to send the message.
        context : django.template.Context
            A context for template rendering.

        """
        base_subject = '{{ event.calendar.course.name }} {{ event.title }}'
        if not self.event.documents.count():
            template_name = self.REQUEST_TEMPLATE
            subject = 'Got a {} study guide?'.format(base_subject)
        else:
            template_name = self.PUBLISH_TEMPLATE
            subject = '{} study guide'.format(base_subject)

        subject = Template(subject).render(context)
        body = get_template(template_name).render(context)

        return make_email_message(subject, body,
                                  make_display_email(
                                      self.sender_address,
                                      self.sender_name),
                                  recipient, connection)

    def _context(self):
        """ Template context for this campaign.

        Returns
        -------
        out : dict
            A template context.

        """
        return {
            'event': self.event,
            'documents': self.documents.all(),
            'mchp_base_url': utils.default_site(),
        }

    # def _update_subscribers(self):
    #     """ Update subscribers for this campaign.

    #     """
    #     if self.active():
    #         for student in utils.students_for_event(self.event):
    #             subscriber, created = StudyGuideCampaignSubscriber.objects.get_or_create(
    #                 campaign=self,
    #                 user=student.user)
    #             if created:  # only add if it's not there already
    #                 self.subscribers.add(subscriber)


class StudyGuideMetaCampaign(MetaCampaign):
    """ Campaign builder for study guide mailings.

    Attributes
    ----------
    event : django.db.models.ForeignKey
        An event for this campaign.
    campaigns : django.db.models.ManyToManyField
        Campaigns associated with this builder.
    documents : django.db.models.ManyToManyField
        Documents associated with this builder.

    """
    event = models.ForeignKey(CalendarEvent, primary_key=True)
    campaigns = models.ManyToManyField(StudyGuideCampaign,
                                       # related_name='+',
                                       blank=True,
                                       null=True)
    documents = models.ManyToManyField(Document,
                                       # related_name='+',
                                       blank=True,
                                       null=True)

    def __str__(self):
        return str(self.event)

    def _update_subscribers(self):
        """ Update subscribers for the active campaign.

        """
        try:
            campaign = self.campaigns.latest('when')
        except StudyGuideCampaign.DoesNotExist:
            pass
        else:
            for student in utils.students_for_event(self.event):
                subscriber, created = StudyGuideCampaignSubscriber.objects.get_or_create(
                    campaign=campaign,
                    user=student.user)
                if created:  # only add if it's not there already
                    campaign.subscribers.add(subscriber)

    def _update_documents(self):
        """ Update documents for the next campaign.

        Returns
        -------
        out : bool
            `True` if documents updated, `False` otherwise.

        """
        if self.campaigns.active():
            top_ranked_documents = utils._rank_documents(self.event)
            # [TODO] this is a kludge
            if set(top_ranked_documents) == set(self.documents.all()):
                return False
            print('[DEBUG] Docs changed!  New campaign ahoy!')
            self.documents = top_ranked_documents
        return True

    def _deactivate_campaigns(self):
        """ Deactivate all still-active campaigns.

        Notes
        -----
        The `until` field of each campaign will be set to "now."
        Each campaign will retain its `when` field to indicate
        the rough time of creation.

        This method is not strictly necessary, except to
        indicate for metrics how many campaigns are
        considered "active" at any one time.

        """
        now = timezone.now()
        for campaign in self.campaigns.active():
            campaign.until = now
            campaign.save(update_fields=['until'])

    def update(self):
        """ Update campaigns.

        """
        if self._update_documents():
            # deactivate existing campaigns
            self._deactivate_campaigns()

            campaign = StudyGuideCampaign.objects.create(
                sender_address=self.sender_address,
                sender_name=self.sender_name,
                event=self.event,
                when=timezone.now(),
                until=self.event.start)
            campaign.documents = self.documents.all()
            self.campaigns.add(campaign)

        self._update_subscribers()
