from django.core.management.base import BaseCommand

from campaigns.models import Campaign


class Command(BaseCommand):
    help = 'Send all due campaign e-mails'

    def handle(self, *args, **options):
        from campaigns.models import StudyGuideMetaCampaign
        from campaigns.utils import upcoming_events
        for event in upcoming_events():
            print('hi')
            mcamp = StudyGuideMetaCampaign.objects.get_or_create(event=event
                #event_start
                )[0]
            mcamp.blast(force=True)

        for campaign in Campaign.objects.all():
            campaign.blast()
