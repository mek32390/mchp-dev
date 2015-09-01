# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0002_auto_20150831_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='RosterExamEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('roster', models.ForeignKey(to='rosters.Roster', related_name='exams')),
            ],
            options={
                'verbose_name': 'roster exam entry',
                'verbose_name_plural': 'roster exam entries',
            },
            bases=(models.Model,),
        ),
    ]
