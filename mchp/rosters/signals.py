from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver
from django.dispatch import Signal

from rosters.models import Roster
from rosters.tasks import approve_roster, extract_roster

import logging
from mchp.celery import debug_task

logger = logging.getLogger(__name__)

roster_uploaded = Signal(providing_args=['roster'])

@receiver(post_save, sender=Roster)
def create_preview_task(sender, instance, **kwargs):

    # this queues a celery task
    try:
        # queue task after 5 seconds
        print("roster post-save")
        extract_roster.apply_async(args=[instance], countdown=5, link_error=debug_task.s())
        # create_preview(instance)
    except OSError:
        logger.error('Celery does not seem to be running')
        # no thumbs for you (start celery/MQ process)
        pass