from django.core.management.base import BaseCommand

from studyguides.models import StudyGuideMetaCampaign
from studyguides.utils import upcoming_events
from django.utils import timezone


class Command(BaseCommand):
    help = 'Prepare and update study guide campaigns'

    def handle(self, *args, **options):
        for event in upcoming_events():
            if event.notify_lead:
                mcamp, _ = StudyGuideMetaCampaign.objects.get_or_create(
                    event=event, defaults={
                        'when': timezone.now(),
                        'sender_address': 'study@mycollegehomepage.com',
                        'sender_name': 'mchp',
                    })
                mcamp.update()

        for campaign in StudyGuideMetaCampaign.objects.active():
            campaign.blast()
            break  # [TODO] DEBUG: remove this line for production
