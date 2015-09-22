# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0006_auto_20150917_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rosterinstructorentry',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rosterinstructorentry',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rosterstudententry',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rosterstudententry',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
