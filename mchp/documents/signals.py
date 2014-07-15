from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver

from documents.models import Document, PREVIEW_LOCATION
from documents.tasks import create_preview

import os.path

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

    # add generated preview filename
    preview = PREVIEW_LOCATION + "/{}_preview.png".format(
        os.path.splitext(instance.filename())[0]
    )
    logger.debug("preview loc " + preview)
    instance.preview = preview
    instance.save()

    # create_preview.delay(instance)
    create_preview(instance)

# Receive the pre_delete signal and delete the file associated with the model instance.
@receiver(post_delete, sender=Document)
def document_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.document:
        instance.document.delete(False)
    if instance.preview:
        instance.preview.delete(False)
