from django.core.management.base import BaseCommand
# from django.utils import timezone

from campaigns.models import CampaignMailer


class Command(BaseCommand):
    help = 'Send all pending campaigns'

    def handle(self, *args, **options):
        campaigns = CampaignMailer.objects.filter(active=True)
        num_processed = 0
        for campaign in campaigns:
            campaign.send()
            num_processed += 1
        # self.stdout.write('Successfully processed {}/{} campaign(s)'.format(num_sent, campaigns.count()))
