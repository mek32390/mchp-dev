# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150501_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.IntegerField(default=0, choices=[(0, 'Study guide'), (1, 'Syllabus')]),
            preserve_default=True,
        ),
    ]
