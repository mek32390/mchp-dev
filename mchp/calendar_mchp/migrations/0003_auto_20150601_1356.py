# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150501_1535'),
        ('calendar_mchp', '0002_auto_20140919_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='documents',
            field=models.ManyToManyField(blank=True, to='documents.Document', related_name='events', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='notify_lead',
            field=models.PositiveIntegerField(blank=True, default=2880),
            preserve_default=True,
        ),
    ]
