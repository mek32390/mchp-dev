# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations, connection


def delete_corrupted_enrollments(app, schema_editor):
    # Cleaning up corrupted data from production
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM schedule_enrollment
        WHERE
        student_id NOT IN (SELECT id FROM user_profile_student)
        OR
        course_id NOT IN (SELECT id FROM schedule_course)
    """)
    cursor.close()


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20141001_1340'),
    ]

    operations = [
        migrations.RunPython(delete_corrupted_enrollments),
    ]
