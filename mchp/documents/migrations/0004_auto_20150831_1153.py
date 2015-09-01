# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0001_initial'),
        ('documents', '0003_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='approved',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='roster_upload',
            field=models.ForeignKey(to='rosters.Roster', null=True),
            preserve_default=True,
        ),
    ]
