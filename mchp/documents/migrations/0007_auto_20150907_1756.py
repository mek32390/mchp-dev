# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20150831_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='roster',
            field=models.ForeignKey(related_name='syllabus', null=True, to='rosters.Roster'),
        ),
    ]
