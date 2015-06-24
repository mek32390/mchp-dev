# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20141001_1340'),
        ('user_profile', '0002_auto_20140925_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('roster_html', models.TextField(verbose_name='roster HTML')),
                ('parsed_csv', models.TextField(verbose_name='parsed CSV', blank=True)),
                ('emails', models.TextField(verbose_name='filter emails', blank=True)),
                ('when', models.DateTimeField(verbose_name='submitted', auto_now_add=True)),
                ('approved', models.DateTimeField(blank=True, null=True)),
                ('imported', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(to='schedule.Course')),
                ('created_by', models.ForeignKey(to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
