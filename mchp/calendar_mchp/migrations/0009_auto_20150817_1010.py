# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0008_auto_20150816_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='original_event',
            field=models.ForeignKey(null=True, blank=True, to='calendar_mchp.CalendarEvent', default=None, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterField(
            model_name='classcalendar',
            name='original_calendar',
            field=models.ForeignKey(null=True, blank=True, to='calendar_mchp.ClassCalendar', default=None, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
