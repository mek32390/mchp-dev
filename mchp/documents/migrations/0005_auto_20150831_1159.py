# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20150831_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='roster_upload',
            new_name='roster',
        ),
    ]
