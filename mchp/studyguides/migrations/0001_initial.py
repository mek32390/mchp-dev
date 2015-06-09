# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import campaigns.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0003_auto_20150508_1635'),
        ('documents', '0002_auto_20150501_1535'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGuideCampaign',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(blank=True, null=True, verbose_name='campaign end')),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(blank=True, max_length=255)),
                ('template', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('documents', models.ManyToManyField(to='documents.Document', blank=True, null=True, related_name='+')),
            ],
            options={
                'ordering': ('event',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudyGuideCampaignSubscriber',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('uuid', models.CharField(default=campaigns.utils.make_uuid, unique=True, max_length=32)),
                ('notified', models.DateTimeField(blank=True, null=True)),
                ('clicked', models.DateTimeField(blank=True, null=True)),
                ('opened', models.DateTimeField(blank=True, null=True)),
                ('unsubscribed', models.DateTimeField(blank=True, null=True)),
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
                ('until', models.DateTimeField(blank=True, null=True, verbose_name='campaign end')),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(blank=True, max_length=255)),
                ('event', models.ForeignKey(to='calendar_mchp.CalendarEvent', serialize=False, primary_key=True)),
                ('campaigns', models.ManyToManyField(to='studyguides.StudyGuideCampaign', blank=True, null=True)),
                ('documents', models.ManyToManyField(to='documents.Document', blank=True, null=True)),
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
