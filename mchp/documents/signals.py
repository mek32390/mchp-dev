from django.conf import settings
from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver

from documents.models import Document, THUMBNAIL_LOCATION, PREVIEW_LOCATION

import os.path
import subprocess

import logging
logger = logging.getLogger(__name__)

'''
This file get import in __init__.py and handles signals for the documents app
'''

@receiver(post_save, sender=Document)
def create_thumbnail(sender, instance, **kwargs):
    # don't do this more than once 
    if not kwargs['created']:
        return 

    # first make sure dirs exist
    os.makedirs(settings.MEDIA_ROOT + '/' + THUMBNAIL_LOCATION, exist_ok=True)
    os.makedirs(settings.MEDIA_ROOT + '/' + PREVIEW_LOCATION, exist_ok=True)

    # add generated thumbnail filename
    thumbnail = THUMBNAIL_LOCATION + "/{}_thumb.png".format(
        os.path.splitext(instance.filename())[0]
    )
    instance.thumbnail = thumbnail
    # add generated preview filename
    preview = PREVIEW_LOCATION + "/{}_preview.png".format(
        os.path.splitext(instance.filename())[0]
    )
    instance.preview = preview
    instance.save()

    _make_thumb(instance, 64, instance.thumbnail)
    _make_thumb(instance, 500, instance.preview)

def _make_thumb(instance, size, name):
    logger.debug(instance.filetype())
    logger.debug(instance.document)
    tmp_name = 'tmp.pdf'
    unoconv_command = 'unoconv -f pdf -e PageRange=1 --output="{}/{}" "{}/{}" && '.format(
        settings.MEDIA_ROOT,
        tmp_name,
        settings.MEDIA_ROOT,
        instance.document,
    ) + "convert -thumbnail {} -background\
            white {}/{}[0] {}/{}".format( 
                size,
                settings.MEDIA_ROOT, 
                tmp_name,
                settings.MEDIA_ROOT, 
                name)

    pdf_command = "convert -thumbnail {} -background\
            white {}/{}[0] {}/{}".format( 
                size,
                settings.MEDIA_ROOT, 
                instance.document, 
                settings.MEDIA_ROOT, 
                name)

    pic_command = "convert -thumbnail {} -background\
            white {}/{} {}/{}".format( 
                size,
                settings.MEDIA_ROOT, 
                instance.document, 
                settings.MEDIA_ROOT, 
                name)

    empty_command = ''

    command = {
        b'application/pdf': pdf_command,
        b'application/msword': unoconv_command,
        b'text/plain': unoconv_command,
        b'application/vnd.openxmlformats-officedocument.wordprocessingml.document': unoconv_command,

        b'image/jpg': pic_command,
        b'image/png': pic_command,
        # gifs have multiple 'pages' (frames)
        b'image/gif': pdf_command,
        }.get(instance.filetype(), empty_command)

    _convert(command)

# just runs the command passed to it
def _convert(command):
    logger.debug(command)

    proc = subprocess.Popen(command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout_value = proc.communicate()[0]
    logger.debug('stdout: ' + str(stdout_value))

# Receive the pre_delete signal and delete the file associated with the model instance.
@receiver(post_delete, sender=Document)
def document_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.document:
        instance.document.delete(False)
    if instance.thumbnail:
        instance.thumbnail.delete(False)
    if instance.preview:
        instance.preview.delete(False)
