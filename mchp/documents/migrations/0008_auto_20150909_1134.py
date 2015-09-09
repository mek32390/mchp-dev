# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20150907_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.IntegerField(default=0, choices=[(0, 'Study Guide'), (1, 'Syllabus')]),
        ),
    ]
