# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0002_auto_20150831_1604'),
        ('documents', '0003_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='approved',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='roster',
            field=models.ForeignKey(null=True, to='rosters.Roster'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='course',
            field=models.ForeignKey(to='schedule.Course', null=True, on_delete=models.SET(documents.models.get_sentinel_course)),
        ),
    ]
