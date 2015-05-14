from django.db import models
from django.utils import timezone
from campaigns.models import (BaseCampaign, Campaign,
                              CampaignSubscriber, CampaignTemplate)
from calendar_mchp.models import CalendarEvent
from documents.models import Document
from operator import methodcaller

from schedule.models import Enrollment
import smtplib
from . import utils




class StudyGuideCampaignCoordinator(BaseCampaign):
    """ Campaign builder for study guide mailings.

    Attributes
    ----------
    campaign : campaigns.models.Campaign
        A campaign associated with this builder.

    """

    campaigns = models.ManyToManyField(Campaign,
                                       # related_name='+',
                                       blank=True,
                                       null=True)
    documents = models.ManyToManyField(Document,
                                       # related_name='+',
                                       blank=True,
                                       null=True)
    updated = models.DateTimeField(blank=True, null=True)
    event = models.ForeignKey(CalendarEvent, unique=True)

    REQUEST_TEMPLATE_SLUG = 'study-guide-request'
    PUBLISH_TEMPLATE_SLUG = 'study-guide-publish'
    # REQUEST_TEMPLATE = 'campaigns/request_for_study_guide.html'
    # PUBLISH_TEMPLATE = 'campaigns/study_guide.html'

    def __str__(self):
        return str(self.event)

    def _new_campaign_name(self):
        """ Create a new campaign name.

        """
        return str(self)

    def queryset_ranker(self, queryset, score):
        counter = Counter(queryset)
        last_score = score
        for element in queryset:
            position += 1  # for different weightings, could multiply, etc.
            counter[element] += score * position
        return counter

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
                             lambda doc: enrollments.get(student=doc.upload.owner).join_date,
                             score=20)

        scores += utils.rank(documents,
                             lambda doc: doc.rating(),
                             score=10)


        print('DEBUG: SCORES = ' + str(scores))
        # scores += self.queryset_ranker(most_recent, 40)
        # scores += self.queryset_ranker(most_purchased, 30)
        # scores += self.queryset_ranker(uploader_in_class, 20)
        # scores += self.queryset_ranker(best_rated, 10)
        top_score = scores.most_common(1)[0][1]
        return [d for d in documents if scores[d] == top_score]


    def _update_subscribers(self):
        """ Update subscribers for the active campaign.

        """
        campaign = self.campaigns.latest('when')
        for student in utils.students_for_event(self.event):
            subscriber, created = CampaignSubscriber.objects.get_or_create(
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

    def update(self):
        """ Update campaigns.

        """
        if self._update_documents():
            # deactivate existing campaigns
            self._deactivate_campaigns()

            if not self.event.documents.count():
                template_slug = self.REQUEST_TEMPLATE_SLUG
            else:
                template_slug = self.PUBLISH_TEMPLATE_SLUG

            template = CampaignTemplate.objects.get(slug=template_slug)

            campaign = Campaign.objects.create(
                name=self._new_campaign_name(),
                template=template,
                when=timezone.now(),
                until=self.event.start)
            self.campaigns.add(campaign)

        self._update_subscribers()
        self.updated = timezone.now()
        self.save(update_fields=['updated'])
###NOTES:SHOULD BE ABLE TO DELETE ALL RELATED CAMPAIGNS WHEN DELETING COORDINATOR
