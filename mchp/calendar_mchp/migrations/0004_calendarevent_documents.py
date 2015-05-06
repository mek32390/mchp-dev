# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150501_1535'),
        ('calendar_mchp', '0003_calendarevent_notify_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='documents',
            field=models.ManyToManyField(related_name='events', to='documents.Document', blank=True, null=True),
            preserve_default=True,
        ),
    ]
