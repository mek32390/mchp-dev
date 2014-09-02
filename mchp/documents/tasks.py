from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger

from django.conf import settings
from django.core.files.base import File
from django.core.files.images import ImageFile

import urllib.request
import subprocess
import uuid
import os.path

from wand.image import Image

from notification.api import add_notification
from documents.models import Upload

logger = get_task_logger(__name__)

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

    logger.error(instance.filetype)
    if not instance.filetype in filetypes and not instance.filetype in convert_type:
        return

    upload = Upload.objects.get(
        document=instance
    )
    if instance.filetype in convert_type:
        output = 'tmp{}.pdf'.format(uuid.uuid4())
        input = 'old{}'.format(uuid.uuid4())

        urllib.request.urlretrieve(instance.document.url, input)

        unoconv_command = 'unoconv -f pdf --output="{}" "{}" '.format(output, input)
        logger.error('converting {}'.format(unoconv_command))
        _run(unoconv_command)
        new_doc = "{}.pdf".format(
            os.path.splitext(instance.filename())[0]
        )
        logger.error(new_doc)
        instance.document.delete()
        try:
            instance.document.save(new_doc, File(open(output,'rb'), output))
        except FileNotFoundError:
            logger.error('Error converting {}'.format(instance.title))
            add_notification(
                upload.owner.user,
                'Your document, {}, asplode. Try converting it to pdf, or upload something else.'.format(instance.title) 
            )
            instance.delete()
            os.remove(input)
            return
            
        os.remove(input)
        os.remove(output)

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
        os.remove(preview_name)

    instance.document.storage.connection.put_acl(settings.AWS_STORAGE_BUCKET_NAME, 'media/' + instance.document.name, '',
                                               {'x-amz-acl':'private'})


# just runs the command passed to it
def _run(command):
    logger.error(command)

    proc = subprocess.Popen(command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    print(proc.communicate())
    # stdout_value = proc.communicate()[0]
    # stderr_value = proc.communicate()[1]
    # logger.info('stdout: ' + str(stdout_value))
    # logger.error('stderr: ' + str(stderr_value))
