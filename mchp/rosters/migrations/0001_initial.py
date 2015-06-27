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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('roster_html', models.TextField(verbose_name='roster HTML')),
                ('emails', models.TextField(blank=True, verbose_name='filter emails')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='submitted')),
                ('reviewed', models.DateTimeField(blank=True, null=True)),
                ('imported', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(to='schedule.Course')),
                ('created_by', models.ForeignKey(to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RosterEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('profile', models.ForeignKey(blank=True, to='user_profile.Student', null=True)),
                ('roster', models.ForeignKey(related_name='entries', to='rosters.Roster')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
