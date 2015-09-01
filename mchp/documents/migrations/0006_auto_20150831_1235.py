# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_auto_20150831_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='course',
            field=models.ForeignKey(to='schedule.Course', on_delete=models.SET(documents.models.get_sentinel_course), null=True),
        ),
    ]
