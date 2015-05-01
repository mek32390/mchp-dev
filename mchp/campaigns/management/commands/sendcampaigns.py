from django.core.management.base import BaseCommand
from campaigns.models import Campaign


class Command(BaseCommand):
    help = 'Send all pending campaigns'

    def handle(self, *args, **options):
        campaigns = Campaign.objects.filter(sent=None)
        num_sent = 0
        for campaign in campaigns:
            campaign.send()
            num_sent += 1
        self.stdout.write('Processed {} campaign(s)'.format(num_sent))
