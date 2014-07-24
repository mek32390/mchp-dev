from __future__ import absolute_import

from celery import shared_task

from django.core.files.base import File
from django.core.files.images import ImageFile

import urllib.request
import subprocess
import uuid
import os.path

from wand.image import Image

import logging
logger = logging.getLogger(__name__)

@shared_task
def create_preview(instance):
    filetypes = [b'application/pdf', b'image/jpeg', b'image/png', b'image/gif',]
    convert_type = [b'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    b'application/msword',
                    b'application/zip',
                    b'application/CDFV2-corrupt',
                    b'text/plain',
                    b'text/html',
                    b'application/vnd.oasis.opendocument.spreadsheet',
                   ]

    logger.debug(instance.filetype)
    if not instance.filetype in filetypes and not instance.filetype in convert_type:
        return

    if instance.filetype in convert_type:
        output = 'tmp{}.pdf'.format(uuid.uuid4())
        input = 'old{}'.format(uuid.uuid4())

        urllib.request.urlretrieve(instance.document.url, input)

        unoconv_command = 'unoconv -f pdf --output="{}" "{}" '.format(output, input)
        logger.debug('converting {}'.format(unoconv_command))
        _run(unoconv_command)
        new_doc = "{}.pdf".format(
            os.path.splitext(instance.filename())[0]
        )
        logger.debug(new_doc)
        instance.document.delete()
        instance.document.save(new_doc, File(open(output,'rb'), output))
        # os.remove(input)
        # os.remove(output)

    size = 500
    with Image(filename=instance.document.url+'[0]') as img:
        preview_name = '/tmp/tmp{}.png'.format(uuid.uuid4().hex)
        img.save(filename=preview_name)
        img = Image(filename=preview_name)
        img.transform(resize=str(size))
        img.save(filename=preview_name)
        preview = "{}_preview.png".format(
            os.path.splitext(instance.filename())[0]
        )
        instance.preview.save(preview, ImageFile(open(preview_name, 'rb'), preview_name))
        # os.remove(preview_name)

    instance.document.storage.connection.put_acl('mchp-dev', 'media/' + instance.document.name, '',
                                               {'x-amz-acl':'private'})


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
