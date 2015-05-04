# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20140925_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignMailer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('category', models.CharField(max_length=2, choices=[('EV', 'Lead time for event'), ('NL', 'Newsletter')])),
                ('when', models.DateTimeField(verbose_name='send when', null=True, blank=True, help_text='If unset, this mailer will be disabled.')),
                ('until', models.DateTimeField(verbose_name='send until', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=78)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('unsubscribes', models.PositiveIntegerField(default=0)),
                ('recipients', models.ManyToManyField(to='user_profile.Student')),
                ('template', models.ForeignKey(to='campaigns.CampaignTemplate')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsletterCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('unsubscribes', models.PositiveIntegerField(default=0)),
                ('recipients', models.ManyToManyField(to='user_profile.Student')),
                ('template', models.ForeignKey(to='campaigns.CampaignTemplate')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaignmailer',
            name='template',
            field=models.ForeignKey(to='campaigns.CampaignTemplate'),
            preserve_default=True,
        ),
    ]
