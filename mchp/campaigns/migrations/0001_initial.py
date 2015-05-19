# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import campaigns.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('when', models.DateTimeField(null=True, help_text='If field is unset, this campaign will be disabled.', verbose_name='campaign start', blank=True)),
                ('until', models.DateTimeField(null=True, verbose_name='campaign end', blank=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('notified', models.DateTimeField(null=True, blank=True)),
                ('opens', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('unsubscribes', models.PositiveIntegerField(default=0)),
                ('uuid', models.CharField(max_length=32, default=campaigns.models.uuid_default)),
                ('campaign', models.ForeignKey(related_name='subscribers', to='campaigns.Campaign')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignTemplate',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(unique=True, help_text='Used by the campaign automailer.  Change with caution!', max_length=255)),
            ],
            options={
                'ordering': ('name',),
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
