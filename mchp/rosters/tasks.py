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
#
# import logging
# logging.getLogger('celery.task.default').setLevel(logging.DEBUG)
# logging.getLogger().setLevel(logging.DEBUG)
#
# from celery import current_app
# current_app.conf.CELERY_ALWAYS_EAGER = True
# current_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
#
# from celery.utils import LOG_LEVELS
# current_app.conf.CELERYD_LOG_LEVEL = LOG_LEVELS['DEBUG']  # pretty much the same as logging.DEBUG

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


    add_notification(
        roster.created_by.user,
        'Your class set for {}, is approved and published!'.format(roster.course)
    )


def _roster_approved_notify(roster):
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
