from django.core.management.base import BaseCommand

from documents.models import Document
from django.utils import timezone


class Command(BaseCommand):
    help = 'Prepare and update models'

    def handle(self, *args, **options):
        for roster in Document.objects.all:
            imported = roster.process()
            if imported > 0:
                roster.status = Roster.IMPORTED
                roster.save(update_fields=['status'])
            print('Imported {} users'.format(imported))