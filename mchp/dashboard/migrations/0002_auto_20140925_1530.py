# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashevent',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'calendar purchase'), (1, 'calendar add'), (2, 'document purchase'), (3, 'document add'), (4, 'other class join'), (5, 'class join'), (6, 'subscription')]),
        ),
    ]
