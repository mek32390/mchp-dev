# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0006_auto_20150901_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='RosterEventEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('roster', models.ForeignKey(to='rosters.Roster', related_name='events')),
            ],
            options={
                'verbose_name': 'roster event entry',
                'verbose_name_plural': 'roster event entries',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='rosterexamentry',
            name='roster',
        ),
        migrations.DeleteModel(
            name='RosterExamEntry',
        ),
    ]
