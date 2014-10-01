# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_auto_20140925_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ('name',)},
        ),
    ]
