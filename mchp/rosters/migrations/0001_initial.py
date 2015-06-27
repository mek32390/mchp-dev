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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('roster_html', models.TextField(verbose_name='roster HTML')),
                ('emails', models.TextField(blank=True, verbose_name='filter emails')),
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
        migrations.CreateModel(
            name='RosterInstructorEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('profile', models.ForeignKey(to='user_profile.Student', null=True, blank=True)),
                ('roster', models.ForeignKey(related_name='instructors', to='rosters.Roster')),
            ],
            options={
                'verbose_name_plural': 'roster instructor entries',
                'verbose_name': 'roster instructor entry',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RosterStudentEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('profile', models.ForeignKey(to='user_profile.Student', null=True, blank=True)),
                ('roster', models.ForeignKey(related_name='students', to='rosters.Roster')),
            ],
            options={
                'verbose_name_plural': 'roster student entries',
                'verbose_name': 'roster student entry',
            },
            bases=(models.Model,),
        ),
    ]
