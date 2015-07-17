from django.core.management.base import BaseCommand

from rosters.models import Roster
from django.utils import timezone


class Command(BaseCommand):
    help = 'Prepare and update study guide campaigns'

    def handle(self, *args, **options):
<<<<<<< HEAD
        for r in Roster.objects.filter(imported=None).exclude(approved=None):
            imported = r.import_roster()
=======
        for roster in Roster.objects.filter(status=Roster.APPROVED):
            imported = roster.process()
            if imported > 0:
                roster.status = Roster.IMPORTED
                roster.save(update_fields=['status'])
>>>>>>> fb3334ddd3a28741912fc30e5ab45a59d56c00cd
            print('Imported {} users'.format(imported))
