from django.core.management.base import BaseCommand

from studyguides.models import StudyGuideMetaCampaign
from studyguides.utils import upcoming_events


class Command(BaseCommand):
    help = 'Prepare and update study guide campaigns'

    def handle(self, *args, **options):
        for event in upcoming_events():
            if event.notify_lead:
                mcamp = StudyGuideMetaCampaign.objects.get_or_create(
                    event=event)[0]
                mcamp.update()
        for campaign in StudyGuideMetaCampaign.objects.active():
            campaign.blast()
