# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='student',
            field=models.ForeignKey(default=None, to='user_profile.Student', related_name='student_sections'),
            preserve_default=False,
        ),
    ]
