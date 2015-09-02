# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0001_initial'),
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
                'verbose_name_plural': 'roster exam entries',
                'verbose_name': 'roster exam entry',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rosterinstructorentry',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rosterstudententry',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
