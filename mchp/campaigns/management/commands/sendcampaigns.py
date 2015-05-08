from django.core.management.base import BaseCommand

from campaigns.models import Campaign


class Command(BaseCommand):
    help = 'Send all due campaign e-mails'

    def handle(self, *args, **options):
        from campaigns.models import StudyGuideCampaignCoordinator
        from campaigns.utils import upcoming_events
        for event in upcoming_events():
            if event.notify_lead:
                mcamp = StudyGuideCampaignCoordinator.objects.get_or_create(
                    event=event)[0]
                mcamp.update()

        for campaign in Campaign.objects.active():
            campaign.blast()
