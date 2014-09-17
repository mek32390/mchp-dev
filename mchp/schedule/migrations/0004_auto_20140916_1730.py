# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20140916_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='group',
            new_name='course_group',
        ),
    ]
