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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('roster_html', models.TextField(verbose_name='roster HTML')),
                ('created', models.DateTimeField(verbose_name='first created', auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('status', models.CharField(max_length=1, default='p', choices=[('p', 'Pending'), ('a', 'Approved'), ('r', 'Rejected'), ('i', 'Imported')])),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('profile', models.ForeignKey(null=True, to='user_profile.Student', blank=True)),
                ('roster', models.ForeignKey(to='rosters.Roster', related_name='instructors')),
            ],
            options={
                'verbose_name': 'roster instructor entry',
                'verbose_name_plural': 'roster instructor entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RosterStudentEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('profile', models.ForeignKey(null=True, to='user_profile.Student', blank=True)),
                ('roster', models.ForeignKey(to='rosters.Roster', related_name='students')),
            ],
            options={
                'verbose_name': 'roster student entry',
                'verbose_name_plural': 'roster student entries',
            },
            bases=(models.Model,),
        ),
    ]