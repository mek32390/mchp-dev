from __future__ import absolute_import
import json

from celery import shared_task, task, Task
from celery.utils.log import get_task_logger
from celery.utils.timeutils import timezone

from django.conf import settings
from django.core.files.base import File
from django.core.files.images import ImageFile

import urllib.request
import subprocess
import uuid
import os.path

from django.db import models

from notification.api import add_notification
from documents.models import Upload
from lib.utils import send_email_for
from schedule.models import Course, Enrollment
from rosters import utils, models as rostermodels
from pywapi import unicode
from . import utils

from pprint import pprint


logger = get_task_logger(__name__)

@shared_task()
def extract_roster(roster):
    """
    WIP
    """

    roster_html = roster.roster_html
    instructor_emails = roster.instructor_emails
    parsed_csv = utils.roster_html_to_csv(roster_html)

    rostermodels.RosterStudentEntry.objects.filter(roster=roster).delete()
    
    for initial_data in utils.csv_string_to_python(parsed_csv):
        # n.b.: emails from instructor emails are not filtered here
        email = initial_data.get('email')
        # don't add entry if email is in instructors
        if email not in instructor_emails:
            params = {
                'first_name': initial_data.get('first'),
                'last_name': initial_data.get('last'),
                'email': email,
                'roster': roster,
                'approved': False
            }
            if email:
                user = utils.get_user(email)
                if user:
                    params['profile'] = user.profile_user
            rostermodels.RosterStudentEntry.objects.create(**params)


@shared_task
def approve_roster(roster):
    """
    WIP
    """
    parsed_csv = utils.roster_html_to_csv(roster_html)
    for initial_data in utils.csv_string_to_python(parsed_csv):
        # n.b.: emails from instructor emails are not filtered here
        email = initial_data.get('email')
        # don't add entry if email is in instructors
        if email not in instructor_emails:
            params = {
                'first_name': initial_data.get('first'),
                'last_name': initial_data.get('last'),
                'email': utils.preprocess_email(email),
                'roster': roster,
                'approved': false
            }
            user = utils.get_user(email)
            if user:
                params['profile'] = user.profile_user
            models.RosterStudentEntry.objects.create(**params)

    unoconv_command = 'unoconv -f pdf --output="{}" "{}" '.format(output, input)
    logger.error('converting {}'.format(unoconv_command))
    _run(unoconv_command)
    new_doc = "{}.pdf".format(
        os.path.splitext(instance.filename())[0]
    )
    instance.document.delete()
    try:
        instance.document.save(new_doc, File(open(output, 'rb'), output))
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
        with Image(filename=settings.COLLECTED_DIR + instance.document.url + '[0]') as img:
            logger.error('making thumbnail for: ' + instance.title)
            print('makeing thumbnail for: ' + instance.title)
            preview_name = '/tmp/tmp{}.png'.format(uuid.uuid4().hex)
            img.save(filename=preview_name)
            img = Image(filename=preview_name)
            img.transform(resize=str(size))
            if img.height > 600:
                img.crop(0, 0, 500, 600)
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

    instance.document.storage.connection.put_acl(settings.AWS_STORAGE_BUCKET_NAME, 'media/' + instance.document.name, '',
                                                 {'x-amz-acl': 'private'})
    add_notification(
        upload.owner.user,
        'Your document, {}, is ready to be sold!'.format(instance.title)
    )


def _roster_approved_notify(document):
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
