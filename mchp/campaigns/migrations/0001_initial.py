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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='first created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('when', models.DateTimeField(verbose_name='campaign start', null=True, help_text='If field is unset, this campaign will be disabled.', blank=True)),
                ('until', models.DateTimeField(null=True, verbose_name='campaign end', blank=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'campaign',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignBlast',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('sent', models.DateTimeField(null=True, blank=True)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'blast',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignTemplate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='first created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('subject', models.CharField(max_length=78)),
                ('body', models.TextField()),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'template',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('notified', models.DateTimeField(null=True, blank=True)),
                ('opens', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('campaign', models.ForeignKey(related_name='subscriptions', to='campaigns.Campaign')),
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
            field=models.ManyToManyField(related_name='blasts', to='campaigns.Subscriber', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='subscribers',
            field=models.ManyToManyField(through='campaigns.Subscriber', to='user_profile.Student', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(to='campaigns.CampaignTemplate'),
            preserve_default=True,
        ),
    ]
