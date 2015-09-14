# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0005_roster_instructor_emails'),
        ('schedule', '0011_auto_20150911_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='created_by_roster',
            field=models.ForeignKey(related_name='enrollments', to='rosters.Roster', null=True),
            preserve_default=True,
        ),
    ]
