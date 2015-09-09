# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import copy

from django.db import models, migrations, connection


def create_students_calendars(apps, schema_editor):

    Enrollment = apps.get_model('schedule', 'Enrollment')
    CalendarEvent = apps.get_model('calendar_mchp', 'CalendarEvent')
    ClassCalendar = apps.get_model('calendar_mchp', 'ClassCalendar')
    Subscription = apps.get_model('calendar_mchp', 'Subscription')
    Student = apps.get_model('user_profile', 'Student')
    Course = apps.get_model('schedule', 'Course')

    for enrollment in Enrollment.objects.all():
        student = Student.objects.get(id=enrollment.student.id)
        course = Course.objects.get(id=enrollment.course.id)

        # Forking calendar
        if not ClassCalendar.objects.filter(course=course, owner=student).exists():
            primary_calendar = ClassCalendar.objects.get(primary=True, course=course)

            new_calendar = copy.copy(primary_calendar)
            new_calendar.pk = None
            new_calendar.id = None
            new_calendar.owner_id = student.id
            new_calendar.primary = False
            new_calendar.private = True
            new_calendar.create_date = None
            new_calendar.color = None
            new_calendar.original_calendar_id = primary_calendar.id

            new_calendar.save()

            original_events = primary_calendar.calendarevent_set.all()
            events = []
            for original_event in original_events:
                event = copy.copy(original_event)
                event.pk = None
                event.id = None
                event.calendar = new_calendar
                event.original_event_id = original_event.id
                events.append(event)

            CalendarEvent.objects.bulk_create(events)
            Subscription.objects.get_or_create(
                student_id=student.id,
                calendar_id=new_calendar.id
            )


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0009_auto_20150817_1010'),
        ('schedule', '0011_delete_corrupted_enrollments'),
        ('user_profile', '0003_student_grade_level'),
    ]

    operations = [
        migrations.RunPython(create_students_calendars),
    ]
