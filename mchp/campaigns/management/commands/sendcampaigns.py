from django.core.management.base import BaseCommand
# from django.utils import timezone

from campaigns.models import CampaignMailer


class Command(BaseCommand):
    help = 'Send all due campaign e-mails'

    def handle(self, *args, **options):
        num_processed = 0
        for mailer in CampaignMailer.objects.all():
            if mailer.active():
                mailer.send()
            num_processed += 1
