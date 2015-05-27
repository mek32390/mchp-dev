# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import campaigns.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_mchp', '0003_auto_20150508_1635'),
        ('documents', '0002_auto_20150501_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGuideCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(null=True, blank=True, verbose_name='campaign end')),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('template', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudyGuideCampaignSubscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('uuid', models.CharField(max_length=32, unique=True, default=campaigns.utils.make_uuid)),
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
                ('until', models.DateTimeField(null=True, blank=True, verbose_name='campaign end')),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(max_length=255, blank=True)),
                ('event', models.ForeignKey(primary_key=True, serialize=False, to='calendar_mchp.CalendarEvent')),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('campaigns', models.ManyToManyField(null=True, blank=True, to='studyguides.StudyGuideCampaign')),
                ('documents', models.ManyToManyField(null=True, blank=True, to='documents.Document')),
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
    ]
