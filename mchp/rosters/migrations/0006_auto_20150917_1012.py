# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0005_roster_instructor_emails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roster',
            options={'verbose_name': 'Class Set', 'verbose_name_plural': 'Class Sets'},
        ),
    ]
