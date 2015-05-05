# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20140925_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('when', models.DateTimeField(blank=True, null=True, help_text='If field is unset, this campaign will be disabled.', verbose_name='campaign start')),
                ('until', models.DateTimeField(blank=True, null=True, verbose_name='campaign end')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'campaign',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignBlast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
            ],
            options={
                'ordering': ('-sent',),
                'verbose_name': 'blast',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=78)),
                ('body', models.TextField()),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'template',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('notified', models.DateTimeField(blank=True, null=True)),
                ('opens', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign', related_name='subscriptions')),
                ('student', models.ForeignKey(to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together=set([('student', 'campaign')]),
        ),
        migrations.AddField(
            model_name='campaignblast',
            name='recipients',
            field=models.ManyToManyField(blank=True, to='campaigns.Subscriber'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='subscribers',
            field=models.ManyToManyField(blank=True, to='user_profile.Student', through='campaigns.Subscriber'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(to='campaigns.CampaignTemplate'),
            preserve_default=True,
        ),
    ]
