from django.core.management.base import BaseCommand

from rosters.models import Roster
from django.utils import timezone


class Command(BaseCommand):
    help = 'Prepare and update study guide campaigns'

    def handle(self, *args, **options):
        for roster in Roster.objects.filter(status=Roster.APPROVED):
            imported = roster.process()
            if imported > 0:
                roster.status = Roster.IMPORTED
                roster.save(update_fields=['status'])
            print('Imported {} users'.format(imported))
