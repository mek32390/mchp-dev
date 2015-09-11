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
from lib.utils import send_email_for
from schedule.models import Course, Enrollment

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

    if type(instance.filetype) == str:
        filetype = instance.filetype.encode('utf-8')
    else:
        filetype = instance.filetype

    if not filetype in filetypes and not filetype in convert_type:
        logger.error('unrecognized file type: ' + instance.filetype)
        print('unrecognized file type: ' + instance.filetype)
        return

    upload = Upload.objects.filter(
        document=instance
    )
    if upload.exists():
        upload = upload[0]
    else: 
        upload = None
    if filetype in convert_type:
        logger.error('converting: ' + instance.title)
        print('converting: '+ instance.title)
        output = 'tmp{}.pdf'.format(uuid.uuid4())
        input = '/tmp/old{}'.format(uuid.uuid4())

        try:
            urllib.request.urlretrieve(instance.document.url, input)
        except OSError as e:
            print(str(e))
            logger.error(str(e))
            return

        unoconv_command = 'unoconv -f pdf --output="{}" "{}" '.format(output, input)
        logger.error('converting {}'.format(unoconv_command))
        _run(unoconv_command)
        new_doc = "{}.pdf".format(
            os.path.splitext(instance.filename())[0]
        )
        instance.document.delete()
        try:
            instance.document.save(new_doc, File(open(output,'rb'), output))
        except FileNotFoundError:
            logger.error('Error converting {}'.format(instance.title))
            print('error converting ' + instance.title)
            if upload:
                add_notification(
                    upload.owner.user,
                    'Your document, {}, asplode. Try converting it to pdf, or upload something else.'.format(instance.title) 
                )
            else:
                logger.error('Document #{}, {}, has no uploader.'.format(instance.id, instance.title))
            instance.delete()
            os.remove(input)
            return
            
        os.remove(input)
        os.remove(output)
        logger.error('converted: ' + instance.title)
        print('converted: ' + instance.title)

    size = 500
    try:
        with Image(filename=settings.COLLECTED_DIR+instance.document.url+'[0]') as img:
            logger.error('making thumbnail for: ' + instance.title)
            print('makeing thumbnail for: ' + instance.title)
            preview_name = '/tmp/tmp{}.png'.format(uuid.uuid4().hex)
            img.save(filename=preview_name)
            img = Image(filename=preview_name)
            img.transform(resize=str(size))
            if img.height > 600:
                img.crop(0,0,500,600)
            img.save(filename=preview_name)
            preview = "{}_preview.png".format(
                os.path.splitext(instance.filename())[0]
            )
            try:
                instance.preview.save(preview, ImageFile(open(preview_name, 'rb'), preview_name))
            except Exception as e:
                logger.error(str(e))
                print(str(e))
            os.remove(preview_name)
            logger.error('made thumbnail for: ' + instance.title)
            print('made thumbnail for: ' + instance.title)
    except Exception as e: 
        logger.error(str(e))
        print(str(e))

    if 'connection' in instance.document.storage:
        instance.document.storage.connection.put_acl(settings.AWS_STORAGE_BUCKET_NAME, 'media/' + instance.document.name, '', {'x-amz-acl':'private'})

    add_notification(
        upload.owner.user,
        'Your document, {}, is ready to be sold!'.format(instance.title) 
    )

def _document_notify(document):
    template = 'email/document_uploaded'
    context = {
        'document': document,
        'course': document.course,
    }
    students = Course.objects.get_classlist_for(document.course)
    logger.info(students)
    enrollment = Enrollment.objects.filter(
        course=document.course,
        student__in=students,
        receive_email=True,
    )
    users = [enroll.student.user for enroll in enrollment]
    send_email_for(template, context, users)

# just runs the command passed to it
def _run(command):
    logger.error(command)

    proc = subprocess.Popen(command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    print('stderr: ' + str(err))
    print('stdout: ' + str(out))
