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
                ('when', models.DateTimeField(help_text='If field is unset, this campaign will be disabled.', verbose_name='campaign start', blank=True, null=True)),
                ('until', models.DateTimeField(null=True, verbose_name='campaign end', blank=True)),
                ('name', models.CharField(max_length=255)),
                ('constituents', models.ManyToManyField(to='user_profile.Student')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignBlast',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sent', models.DateTimeField(null=True, blank=True)),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
                ('recipients', models.ManyToManyField(to='user_profile.Student', related_name='blasts')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('subject', models.CharField(max_length=78)),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'template',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(to='campaigns.CampaignTemplate'),
            preserve_default=True,
        ),
    ]
