# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0005_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='RosterExamEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
        migrations.RemoveField(
            model_name='rosterevententry',
            name='roster',
        ),
        migrations.DeleteModel(
            name='RosterEventEntry',
        ),
    ]
