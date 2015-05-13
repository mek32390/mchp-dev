from django.core.management.base import BaseCommand

from studyguides.models import StudyGuideCampaignCoordinator
from studyguides.utils import upcoming_events


class Command(BaseCommand):
    help = 'Prepare and update study guide campaigns'

    def handle(self, *args, **options):
        for event in upcoming_events():
            if event.notify_lead:
                mcamp = StudyGuideCampaignCoordinator.objects.get_or_create(
                    event=event)[0]
                mcamp.update()
