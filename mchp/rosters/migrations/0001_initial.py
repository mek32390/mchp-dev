# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20140925_0029'),
        ('schedule', '0010_auto_20141001_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('source', models.TextField(verbose_name='source code')),
                ('emails', models.TextField(verbose_name='filter emails', blank=True)),
                ('when', models.DateTimeField(verbose_name='submitted', auto_now_add=True)),
                ('approved', models.DateTimeField(null=True, blank=True)),
                ('imported', models.DateTimeField(null=True, blank=True)),
                ('course', models.ForeignKey(to='schedule.Course')),
                ('created_by', models.ForeignKey(to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
