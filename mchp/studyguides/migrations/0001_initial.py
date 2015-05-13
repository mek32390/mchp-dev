# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150501_1535'),
        ('campaigns', '0001_initial'),
        ('calendar_mchp', '0003_auto_20150508_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGuideCampaignCoordinator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('when', models.DateTimeField(help_text='If field is unset, this campaign will be disabled.', blank=True, null=True, verbose_name='campaign start')),
                ('until', models.DateTimeField(blank=True, null=True, verbose_name='campaign end')),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('campaigns', models.ManyToManyField(to='campaigns.Campaign', blank=True, null=True)),
                ('documents', models.ManyToManyField(to='documents.Document', blank=True, null=True)),
                ('event', models.ForeignKey(unique=True, to='calendar_mchp.CalendarEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
