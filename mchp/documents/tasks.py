from __future__ import absolute_import

from celery import shared_task

from django.core.files.images import ImageFile

import subprocess
import uuid
import os.path

from wand.image import Image

import logging
logger = logging.getLogger(__name__)

@shared_task
def create_preview(instance):
    filetypes = [b'application/pdf', b'image/jpeg', b'image/png', b'image/gif',]

    logger.debug(instance.filetype)
    if not instance.filetype in filetypes:
        return

    size = 500
    with Image(filename=instance.document.url+'[0]') as img:
        logger.debug(img)
        preview_name = 'tmp{}.png'.format(uuid.uuid4().hex)
        img.save(filename=preview_name)
        img = Image(filename=preview_name)
        img.transform(resize=str(size))
        img.save(filename=preview_name)
        preview = "{}_preview.png".format(
            os.path.splitext(instance.filename())[0]
        )
        instance.preview.save(preview, ImageFile(open(preview_name, 'rb'), preview_name))
        os.remove(preview_name)

    instance.document.storage.connection.put_acl('mchp-dev', 'media/' + instance.document.name, '',
                                               {'x-amz-acl':'private'})

    # logger.debug(instance.filetype)
    # logger.debug(instance.document)
    # tmp_name = 'tmp.pdf'
    # unoconv_command = 'unoconv -f pdf -e PageRange=1 --output="{}{}" "{}{}" && '.format(
    #     settings.MEDIA_URL,
    #     tmp_name,
    #     settings.MEDIA_URL,
    #     instance.document,
    # ) + "convert -thumbnail {} -background\
    #         white {}{}[0] {}{}".format( 
    #             size,
    #             settings.MEDIA_URL, 
    #             tmp_name,
    #             settings.MEDIA_URL, 
    #             name)

    # pdf_command = "convert -thumbnail {} -background\
    #         white {}{}[0] {}{}".format( 
    #             size,
    #             settings.MEDIA_URL, 
    #             instance.document, 
    #             settings.MEDIA_URL, 
    #             name)

    # pic_command = "convert -thumbnail {} -background\
    #         white {}{} {}{}".format( 
    #             size,
    #             settings.MEDIA_URL, 
    #             instance.document, 
    #             settings.MEDIA_URL, 
    #             name)

    # empty_command = ''

    # command = {
    #     b'application/pdf': pdf_command,
    #     b'application/msword': unoconv_command,
    #     b'text/plain': unoconv_command,
    #     b'application/vnd.openxmlformats-officedocument.wordprocessingml.document': unoconv_command,

    #     # TODO: the normal pics can just use a pic.thumbnail function call i think
    #     b'image/jpg': pic_command,
    #     b'image/png': pic_command,
    #     # gifs have multiple 'pages' (frames)
    #     b'image/gif': pdf_command,
    #     }.get(instance.filetype, empty_command)

    # _convert(command)

# just runs the command passed to it
def _run(command):
    logger.debug(command)

    proc = subprocess.Popen(command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout_value = proc.communicate()[0]
    logger.debug('stdout: ' + str(stdout_value))
