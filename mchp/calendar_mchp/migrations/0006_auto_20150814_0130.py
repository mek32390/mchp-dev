# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0005_create_calendars_for_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classcalendar',
            name='color',
            field=models.CharField(blank=True, max_length=7),
        ),
    ]
