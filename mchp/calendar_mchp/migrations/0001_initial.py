# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_section_student'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('all_day', models.BooleanField(default=False)),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('url', models.URLField(blank=True)),
                ('is_recurring', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassCalendar',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=2000, blank=True)),
                ('private', models.BooleanField(default=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('accuracy', models.FloatField(default=-1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('expire_date', models.DateTimeField()),
                ('color', models.CharField(default='#FFFFFF', max_length=7, blank=True)),
                ('course', models.ForeignKey(to='schedule.Course', related_name='calendar_courses')),
                ('owner', models.ForeignKey(to='user_profile.Student', related_name='calendars')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=1)),
                ('payment_date', models.DateTimeField()),
                ('subscribe_date', models.DateTimeField(auto_now_add=True)),
                ('enabled', models.BooleanField(default=True)),
                ('accuracy', models.SmallIntegerField(default=-1)),
                ('calendar', models.ForeignKey(to='calendar_mchp.ClassCalendar')),
                ('student', models.ForeignKey(to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='classcalendar',
            name='subscribers',
            field=models.ManyToManyField(to='user_profile.Student', through='calendar_mchp.Subscription'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='classcalendar',
            unique_together=set([('owner', 'course')]),
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='calendar',
            field=models.ForeignKey(to='calendar_mchp.ClassCalendar'),
            preserve_default=True,
        ),
    ]
