# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta
from django.utils import timezone

from django.db import models, migrations
from django.db.models import Count
from calendar_mchp.utils import generate_calendar_color
from mchp import settings


def create_calendars(apps, schema_editor):
    Student = apps.get_model('user_profile', 'Student')
    Course = apps.get_model('schedule', 'Course')
    ClassCalendar = apps.get_model('calendar_mchp', 'ClassCalendar')

    courses_with_no_calendars = Course.objects.annotate(num_courses=Count('calendar_courses')).filter(num_courses=0)
    if not courses_with_no_calendars.exists():
        # Nothing to migrate
        return

    admin_user = Student.objects.filter(user__username='mchp')
    if admin_user.exists():
        admin_user = admin_user[0]
    else:
        admin_user = Student.objects.filter(user__is_superuser=True)
        if admin_user.exists():
            admin_user = admin_user[0]
        else:
            raise Exception("There is no 'mchp' user or any other superuser to attach calendars to.")

    existing_calendars = list(ClassCalendar.objects.filter(owner=admin_user))
    courses_with_no_calendars = Course.objects.annotate(num_courses=Count('calendar_courses')).filter(num_courses=0)

    for course in courses_with_no_calendars:
        calendar = ClassCalendar()
        calendar.course = course
        calendar.owner = admin_user
        calendar.description = ''
        calendar.private = False
        calendar.primary = True
        calendar.color = generate_calendar_color(existing_calendars)
        calendar.title = str(course.dept) + " " + str(course.course_number)

        calendar.end_date = timezone.now() + timedelta(days=365 * 5) # off-setting to 5 years
        calendar.end_date = calendar.end_date.replace(hour=11, minute=59)

        calendar.expire_date = timezone.now() + settings.MCHP_PRICING['calendar_expiration']

        calendar.save()

        existing_calendars.append(calendar)


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0004_classcalendar_primary'),
    ]

    operations = [
        migrations.RunPython(create_calendars),
    ]
