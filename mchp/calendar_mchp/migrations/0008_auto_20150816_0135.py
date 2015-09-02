# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0007_auto_20150816_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='original_event',
            field=models.ForeignKey(default=None, null=True, to='calendar_mchp.CalendarEvent', blank=True),
        ),
        migrations.AlterField(
            model_name='classcalendar',
            name='original_calendar',
            field=models.ForeignKey(default=None, null=True, to='calendar_mchp.ClassCalendar', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='classcalendar',
            unique_together=None,
        ),
    ]
