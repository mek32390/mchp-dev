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
    name : django.db.models.CharField
        An internal name to identify this campaign.
    template : django.db.models.CharField
        A template associated with this campaign.
    subject : django.db.models.CharField
        A subject line associated with this campaign.

    """
    name = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

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

        subject = Template(self.subject).render(context)
        body = get_template(self.template).render(context)

        return make_email_message(subject, body,
                                  make_display_email(
                                      self.sender_address,
                                      self.sender_name),
                                  recipient, connection)

    def unsubscribed(self):
        """ How many subscribers have unsubscribed from their messages? """
        return self.subscribers.objects.exclude(unsubscribed=None).count()


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
    updated = django.db.models.DateTimeField
        When was this campaign last updated?

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
    updated = models.DateTimeField(blank=True, null=True)

    REQUEST_TEMPLATE = 'studyguides/request_for_study_guide.html'
    PUBLISH_TEMPLATE = 'studyguides/study_guide.html'

    def __str__(self):
        return str(self.event)

    def _new_campaign_name(self):
        """ Create a new campaign name.

        """
        return str(self)

    def _filter_current_documents(self):
        """ Return likely primary document candidates.

        """
        documents = self.event.documents.all()

        # get all enrollments (student and join date)
        enrollments = Enrollment.objects.filter(
            course=self.event.calendar.course)

        scores = utils.rank(documents, None)

        scores += utils.rank(documents,
                             lambda doc: doc.create_date,
                             score=40)

        scores += utils.rank(documents,
                             lambda doc: doc.purchased_document.count(),
                             score=30)

        scores += utils.rank(documents,
                             lambda doc: enrollments.get(
                                 student=doc.upload.owner).join_date,
                             score=20)

        scores += utils.rank(documents,
                             lambda doc: doc.rating(),
                             score=10)

        print('DEBUG: SCORES = ' + str(scores))
        top_score = scores.most_common(1)
        if top_score:
            top_score = top_score[0][1]
            return [d for d in documents if scores[d] == top_score]
        else:
            return []

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
        primary_documents = self._filter_current_documents()
        # [TODO] this is a kludge
        if set(primary_documents) != set(self.documents.all()):
            print('[DEBUG] Docs changed!  New campaign ahoy!')
            self.documents = primary_documents
            return True
        elif not self.campaigns.active():
            return True
        else:
            return False

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

    def blast(self, context=None, force=False):
        """ Send a blast to this campaign.

        Parameters
        ----------
        context : dict, optional
            A dictionary to turn into context variables for the message.
        force : bool, optional
            `True` to notify subscribers who have already been notified,
            `False` otherwise.  Default `False`.

        """
        if not context:
            context = {}
        context.update(documents=self.documents, event=self.event)
        for campaign in self.campaigns.active():
            campaign.blast(context=context, force=force)

    def update(self):
        """ Update campaigns.

        """
        if self._update_documents():
            # deactivate existing campaigns
            self._deactivate_campaigns()

            base_subject = '{{ event.calendar.course.name }} {{ event.title }}'
            if not self.event.documents.count():
                template_name = self.REQUEST_TEMPLATE
                subject = 'Got a {} study guide?'.format(base_subject)
            else:
                template_name = self.PUBLISH_TEMPLATE
                subject = '{} study guide'.format(base_subject)

            campaign = StudyGuideCampaign.objects.create(
                name=self._new_campaign_name(),
                template=template_name,
                subject=subject,
                sender_address=self.sender_address,
                sender_name=self.sender_name,
                when=timezone.now(),
                until=self.event.start)
            self.campaigns.add(campaign)

        self._update_subscribers()
        self.updated = timezone.now()
        self.save(update_fields=['updated'])
