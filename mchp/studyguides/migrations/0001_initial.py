# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_mchp', '0003_auto_20150508_1635'),
        ('documents', '0002_auto_20150501_1535'),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGuideAnnouncement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('template', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
                ('documents', models.ManyToManyField(blank=True, related_name='+', null=True, to='documents.Document')),
            ],
            options={
                'ordering': ('event',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudyGuideMetaCampaign',
            fields=[
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(blank=True, verbose_name='campaign end', null=True)),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(blank=True, max_length=255)),
                ('event', models.ForeignKey(primary_key=True, serialize=False, to='calendar_mchp.CalendarEvent')),
                ('campaigns', models.ManyToManyField(blank=True, through='studyguides.StudyGuideAnnouncement', null=True, to='campaigns.Campaign')),
                ('documents', models.ManyToManyField(blank=True, related_name='+', null=True, to='documents.Document')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studyguideannouncement',
            name='event',
            field=models.ForeignKey(to='calendar_mchp.CalendarEvent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studyguideannouncement',
            name='metacampaign',
            field=models.ForeignKey(to='studyguides.StudyGuideMetaCampaign'),
            preserve_default=True,
        ),
    ]
