# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_auto_20140925_1744'),
        ('dashboard', '0002_auto_20140925_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsstype',
            name='school',
            field=models.ForeignKey(null=True, to='schedule.School', blank=True, default=None),
            preserve_default=True,
        ),
    ]
