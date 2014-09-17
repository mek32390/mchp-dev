# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_section_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Major',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='zip_code',
            new_name='zipcode',
        ),
        migrations.AddField(
            model_name='course',
            name='group',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
