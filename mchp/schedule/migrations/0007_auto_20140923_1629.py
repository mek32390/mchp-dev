# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20140923_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolemail',
            name='school',
            field=models.ForeignKey(blank=True, null=True, to='schedule.School', related_name='school_email'),
        ),
    ]
