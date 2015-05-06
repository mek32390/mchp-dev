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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('when', models.DateTimeField(blank=True, verbose_name='campaign start', null=True, help_text='If field is unset, this campaign will be disabled.')),
                ('until', models.DateTimeField(blank=True, verbose_name='campaign end', null=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
            name='CampaignTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('subject', models.CharField(max_length=78)),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'template',
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('notified', models.DateTimeField(blank=True, null=True)),
                ('opens', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign', related_name='subscribers')),
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
            field=models.ManyToManyField(to='campaigns.Subscriber', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(to='campaigns.CampaignTemplate'),
            preserve_default=True,
        ),
    ]
