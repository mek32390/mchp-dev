from django.core.management.base import BaseCommand

from rosters.models import Roster
from django.utils import timezone


class Command(BaseCommand):
    help = 'Prepare and update study guide campaigns'

    def handle(self, *args, **options):
        for r in Roster.objects.filter(imported=None).exclude(approved=None):
            imported = r.import_roster()
            print('Imported {} users'.format(imported))
