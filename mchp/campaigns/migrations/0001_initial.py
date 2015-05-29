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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('when', models.DateTimeField(verbose_name='campaign start')),
                ('until', models.DateTimeField(null=True, verbose_name='campaign end', blank=True)),
                ('sender_address', models.EmailField(max_length=254)),
                ('sender_name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignSubscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('uuid', models.CharField(unique=True, max_length=32, default=campaigns.utils.make_uuid)),
                ('notified', models.DateTimeField(null=True, blank=True)),
                ('clicked', models.DateTimeField(null=True, blank=True)),
                ('opened', models.DateTimeField(null=True, blank=True)),
                ('unsubscribed', models.DateTimeField(null=True, blank=True)),
                ('campaign', models.ForeignKey(related_name='subscribers', to='campaigns.Campaign')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='campaignsubscriber',
            unique_together=set([('campaign', 'user')]),
        ),
    ]
