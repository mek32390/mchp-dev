# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import campaigns.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150501_1535'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_mchp', '0003_auto_20150601_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGuideCampaign',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(null=True, verbose_name='campaign end', blank=True)),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(max_length=255, blank=True)),
                ('template', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('documents', models.ManyToManyField(to='documents.Document', null=True, related_name='+', blank=True)),
            ],
            options={
                'ordering': ('event',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudyGuideCampaignSubscriber',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('uuid', models.CharField(max_length=32, default=campaigns.utils.make_uuid, unique=True)),
                ('notified', models.DateTimeField(null=True, blank=True)),
                ('clicked', models.DateTimeField(null=True, blank=True)),
                ('opened', models.DateTimeField(null=True, blank=True)),
                ('unsubscribed', models.DateTimeField(null=True, blank=True)),
                ('campaign', models.ForeignKey(to='studyguides.StudyGuideCampaign', related_name='subscribers')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudyGuideMetaCampaign',
            fields=[
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(null=True, verbose_name='campaign end', blank=True)),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(max_length=255, blank=True)),
                ('event', models.ForeignKey(serialize=False, primary_key=True, to='calendar_mchp.CalendarEvent')),
                ('campaigns', models.ManyToManyField(to='studyguides.StudyGuideCampaign', null=True, blank=True)),
                ('documents', models.ManyToManyField(to='documents.Document', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='studyguidecampaignsubscriber',
            unique_together=set([('campaign', 'user')]),
        ),
        migrations.AddField(
            model_name='studyguidecampaign',
            name='event',
            field=models.ForeignKey(to='calendar_mchp.CalendarEvent'),
            preserve_default=True,
        ),
    ]
