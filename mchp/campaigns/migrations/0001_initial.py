# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150501_1535'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_mchp', '0003_auto_20150508_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('when', models.DateTimeField(null=True, blank=True, help_text='If field is unset, this campaign will be disabled.', verbose_name='campaign start')),
                ('until', models.DateTimeField(null=True, blank=True, verbose_name='campaign end')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignSubscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('notified', models.DateTimeField(null=True, blank=True)),
                ('opens', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign', related_name='subscribers')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(help_text='Used by the campaign automailer.  Change with caution!', unique=True, max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudyGuideCampaignCoordinator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('when', models.DateTimeField(null=True, blank=True, help_text='If field is unset, this campaign will be disabled.', verbose_name='campaign start')),
                ('until', models.DateTimeField(null=True, blank=True, verbose_name='campaign end')),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('campaigns', models.ManyToManyField(null=True, blank=True, to='campaigns.Campaign')),
                ('documents', models.ManyToManyField(null=True, blank=True, to='documents.Document')),
                ('event', models.ForeignKey(to='calendar_mchp.CalendarEvent', unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='campaignsubscriber',
            unique_together=set([('campaign', 'user')]),
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(to='campaigns.CampaignTemplate'),
            preserve_default=True,
        ),
    ]
