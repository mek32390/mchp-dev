# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0002_auto_20140919_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='notify_lead',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
