# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('when', models.DateTimeField(blank=True, help_text='If field is unset, this campaign will be disabled.', null=True, verbose_name='campaign start')),
                ('until', models.DateTimeField(blank=True, null=True, verbose_name='campaign end')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'campaign',
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignBlast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
            ],
            options={
                'verbose_name': 'blast',
                'ordering': ('-sent',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignSubscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('notified', models.DateTimeField(blank=True, null=True)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'template',
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='campaignsubscriber',
            unique_together=set([('campaign', 'user')]),
        ),
        migrations.AddField(
            model_name='campaignblast',
            name='recipients',
            field=models.ManyToManyField(blank=True, to='campaigns.CampaignSubscriber'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(to='campaigns.CampaignTemplate'),
            preserve_default=True,
        ),
    ]
