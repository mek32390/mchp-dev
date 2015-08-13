# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0003_auto_20150601_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='classcalendar',
            name='primary',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
