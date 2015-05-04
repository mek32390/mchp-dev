# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventCampaignMailer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=78)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsletterCampaignMailer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=78)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('when', models.DateTimeField(verbose_name='send at')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
