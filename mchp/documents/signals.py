from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver

from documents.models import Document
from documents.tasks import create_preview

import logging
logger = logging.getLogger(__name__)

'''
This file gets imported in __init__.py and handles signals for the documents app
'''

@receiver(post_save, sender=Document)
def create_preview_task(sender, instance, **kwargs):
    # don't do this more than once 
    if not kwargs['created']:
        return 

    # this queues a celery task
    try:
        # queue task after 10 seconds
        create_preview.apply_async(args=[instance], countdown=10)
    except OSError:
        # no thumbs for you (start celery/MQ process)
        pass

# Receive the pre_delete signal and delete the file associated with the model instance.
@receiver(post_delete, sender=Document)
def document_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.document:
        instance.document.delete(False)
    if instance.preview:
        instance.preview.delete(False)
