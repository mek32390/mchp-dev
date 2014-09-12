# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageHit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('agent', models.CharField(max_length=300)),
                ('time', models.DateTimeField(verbose_name='date accessed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
