# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0004_auto_20150901_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='roster',
            name='instructor_emails',
            field=models.TextField(default='nomail', verbose_name='instructor emails'),
            preserve_default=False,
        ),
    ]
