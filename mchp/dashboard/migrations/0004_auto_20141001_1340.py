# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rsstype_school'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rsstype',
            options={'ordering': ('link_order', 'name')},
        ),
        migrations.AlterField(
            model_name='rsstype',
            name='link_order',
            field=models.IntegerField(),
        ),
    ]
