from django.core.management.base import BaseCommand

from campaigns.models import Campaign


class Command(BaseCommand):
    help = 'Send all due campaign e-mails'

    def handle(self, *args, **options):
        for campaign in Campaign.objects.active():
            campaign.blast()
