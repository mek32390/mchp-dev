# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classcalendar',
            name='accuracy',
        ),
        migrations.RemoveField(
            model_name='classcalendar',
            name='price',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='accuracy',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='payment_date',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='price',
        ),
    ]
