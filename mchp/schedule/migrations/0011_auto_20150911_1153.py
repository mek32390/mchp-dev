# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20141001_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.CharField(max_length=30),
        ),
    ]
