# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_student_grade_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_by_roster_no_user',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
