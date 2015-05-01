from django.core.management.base import BaseCommand
# from django.utils import timezone

from campaigns.models import EventCampaignMailer


class Command(BaseCommand):
    help = 'Send all pending campaigns'

    def handle(self, *args, **options):
        campaigns = []
        campaigns.extend(EventCampaignMailer.objects.filter(active=True))
        # campaigns.extend(NewsletterCampaignMailer.objects.filter(active=True))
        num_processed = 0
        for campaign in campaigns:
            campaign.send()
            num_processed += 1
