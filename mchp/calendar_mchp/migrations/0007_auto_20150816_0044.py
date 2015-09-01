# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0006_auto_20150814_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='original_event',
            field=models.ForeignKey(null=True, default=None, to='calendar_mchp.CalendarEvent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classcalendar',
            name='original_calendar',
            field=models.ForeignKey(null=True, default=None, to='calendar_mchp.ClassCalendar'),
            preserve_default=True,
        ),
    ]
