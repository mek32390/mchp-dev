from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver
from django.dispatch import Signal

from rosters.models import Roster
from rosters.tasks import approve_roster, extract_roster, reject_roster

import logging
from mchp.celery import debug_task

logger = logging.getLogger(__name__)

roster_uploaded = Signal(providing_args=['roster'])
roster_rejected = Signal(providing_args=['roster'])
roster_approved = Signal(providing_args=['roster'])

def roster_on_create(sender, roster, **kwargs):

    # this queues a celery task
    try:
        # queue task after 5 seconds
        print("roster post-save")
        extract_roster.apply_async(args=[roster], countdown=5, link_error=debug_task.s())
        # create_preview(instance)
    except OSError:
        logger.error('Celery does not seem to be running')
        # no thumbs for you (start celery/MQ process)
        pass

def roster_on_reject(sender, roster, **kwargs):
    try:
        # queue task after 5 seconds
        reject_roster.apply_async(args=[roster], countdown=5, link_error=debug_task.s())
        # create_preview(instance)
    except OSError:
        logger.error('Celery does not seem to be running')
        # no thumbs for you (start celery/MQ process)
        pass

def roster_on_approve(sender, roster, **kwargs):
    try:
        # queue task after 5 seconds
        approve_roster.apply_async(args=[roster], countdown=5, link_error=debug_task.s())
        # create_preview(instance)
    except OSError:
        logger.error('Celery does not seem to be running')
        # no thumbs for you (start celery/MQ process)
        pass


roster_uploaded.connect(roster_on_create)
roster_rejected.connect(roster_on_reject)
roster_approved.connect(roster_on_approve)
