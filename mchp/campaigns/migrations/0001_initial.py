# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import campaigns.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sender', models.EmailField(max_length=254)),
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(verbose_name='campaign end', blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('sender_name', models.CharField(blank=True, max_length=254)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignSubscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=campaigns.utils.make_uuid, max_length=32, unique=True)),
                ('notified', models.DateTimeField(blank=True, null=True)),
                ('clicked', models.DateTimeField(blank=True, null=True)),
                ('opened', models.DateTimeField(blank=True, null=True)),
                ('unsubscribed', models.DateTimeField(blank=True, null=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, help_text='Used by the campaign automailer.  Change with caution!', unique=True)),
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
