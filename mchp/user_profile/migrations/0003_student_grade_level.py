# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20140925_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade_level',
            field=models.IntegerField(choices=[(0, 'Freshman'), (1, 'Sophomore'), (2, 'Junior'), (3, 'Senior'), (4, 'Super-Senior'), (5, 'Graduate')], null=True),
            preserve_default=True,
        ),
    ]
