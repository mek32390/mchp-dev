# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '__first__'),
        ('calendar_mchp', '0001_initial'),
        ('schedule', '0002_section_student'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'calendar purchase'), (1, 'calendar add'), (2, 'document purchase'), (3, 'document add'), (4, 'other class join'), (5, 'class join')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('calendar', models.ForeignKey(null=True, blank=True, to='calendar_mchp.ClassCalendar')),
                ('course', models.ForeignKey(to='schedule.Course')),
                ('document', models.ForeignKey(null=True, blank=True, to='documents.Document')),
                ('event', models.ForeignKey(null=True, blank=True, to='calendar_mchp.CalendarEvent')),
                ('followers', models.ManyToManyField(related_name='followers', to='user_profile.Student')),
                ('student', models.ForeignKey(related_name='target', to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RSSLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField(blank=True)),
                ('story_count', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RSSSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RSSType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=10)),
                ('link_order', models.IntegerField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('zipcode', models.CharField(max_length=11, unique=True)),
                ('info', jsonfield.fields.JSONField()),
                ('fetch', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rsssetting',
            name='rss_type',
            field=models.ForeignKey(to='dashboard.RSSType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rsssetting',
            name='student',
            field=models.ForeignKey(to='user_profile.Student'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='rsssetting',
            unique_together=set([('student', 'rss_type')]),
        ),
        migrations.AddField(
            model_name='rsslink',
            name='rss_type',
            field=models.ForeignKey(to='dashboard.RSSType'),
            preserve_default=True,
        ),
    ]
