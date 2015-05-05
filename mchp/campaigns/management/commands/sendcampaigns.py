from django.core.management.base import BaseCommand

from campaigns.models import Campaign
from campaigns import utils


class Command(BaseCommand):
    help = 'Send all due campaign e-mails'

    def handle(self, *args, **options):
        from campaigns.utils import upcoming_event_subscribers
        recipients = upcoming_event_subscribers()
        for campaign in Campaign.objects.all():
            campaign.constituents = utils.upcoming_event_subscribers()
            campaign.save()
            campaign.blast()
