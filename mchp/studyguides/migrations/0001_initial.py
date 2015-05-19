# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150501_1535'),
        ('calendar_mchp', '0003_auto_20150508_1635'),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGuideCampaignCoordinator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('when', models.DateTimeField(verbose_name='campaign start', blank=True, null=True, help_text='If field is unset, this campaign will be disabled.')),
                ('until', models.DateTimeField(verbose_name='campaign end', blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('campaigns', models.ManyToManyField(to='campaigns.Campaign', blank=True, null=True)),
                ('documents', models.ManyToManyField(to='documents.Document', blank=True, null=True)),
                ('event', models.ForeignKey(to='calendar_mchp.CalendarEvent', unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
