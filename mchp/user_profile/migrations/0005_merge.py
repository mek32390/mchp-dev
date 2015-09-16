# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_student_created_by_roster_no_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrole',
            name='intern_manager',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]