# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import campaigns.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0002_auto_20150501_1535'),
        ('calendar_mchp', '0003_auto_20150508_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGuideCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(blank=True, verbose_name='campaign end', null=True)),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(blank=True, max_length=255)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('uuid', models.CharField(unique=True, max_length=32, default=campaigns.utils.make_uuid)),
                ('notified', models.DateTimeField(blank=True, null=True)),
                ('clicked', models.DateTimeField(blank=True, null=True)),
                ('opened', models.DateTimeField(blank=True, null=True)),
                ('unsubscribed', models.DateTimeField(blank=True, null=True)),
                ('campaign', models.ForeignKey(related_name='subscribers', to='studyguides.StudyGuideCampaign')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudyGuideMetaCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(blank=True, verbose_name='campaign end', null=True)),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(blank=True, max_length=255)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('campaigns', models.ManyToManyField(blank=True, null=True, to='studyguides.StudyGuideCampaign')),
                ('documents', models.ManyToManyField(blank=True, null=True, to='documents.Document')),
                ('event', models.ForeignKey(unique=True, to='calendar_mchp.CalendarEvent')),
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
