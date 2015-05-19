# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
        ('calendar_mchp', '0003_auto_20150508_1635'),
        ('documents', '0002_auto_20150501_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGuideCampaignCoordinator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('when', models.DateTimeField(verbose_name='campaign start', null=True, help_text='If field is unset, this campaign will be disabled.', blank=True)),
                ('until', models.DateTimeField(verbose_name='campaign end', null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('campaigns', models.ManyToManyField(to='campaigns.Campaign', null=True, blank=True)),
                ('documents', models.ManyToManyField(to='documents.Document', null=True, blank=True)),
                ('event', models.ForeignKey(unique=True, to='calendar_mchp.CalendarEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
