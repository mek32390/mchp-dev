from django.core.management.base import BaseCommand

from campaigns.models import Campaign
from datetime import timedelta


class Command(BaseCommand):
    help = 'Send all due campaign e-mails'

    def handle(self, *args, **options):
        from campaigns.models import StudyGuideMetaCampaign
        from campaigns.utils import upcoming_events
        for event in upcoming_events():
            if event.notify_lead:
                lead = timedelta(minutes=event.notify_lead)
                mcamp = StudyGuideMetaCampaign.objects.get_or_create(
                    event=event,
                    when=event.start - lead,
                    until=event.start)[0]
                mcamp.blast()

        for campaign in Campaign.objects.all():
            campaign.blast()
