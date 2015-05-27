# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import campaigns.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(verbose_name='campaign end', null=True, blank=True)),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(max_length=255, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uuid', models.CharField(max_length=32, unique=True, default=campaigns.utils.make_uuid)),
                ('notified', models.DateTimeField(null=True, blank=True)),
                ('clicked', models.DateTimeField(null=True, blank=True)),
                ('opened', models.DateTimeField(null=True, blank=True)),
                ('unsubscribed', models.DateTimeField(null=True, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True)),
                ('name', models.CharField(max_length=255, unique=True)),
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
