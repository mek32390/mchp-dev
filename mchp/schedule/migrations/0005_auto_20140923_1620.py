# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20140916_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_address', models.CharField(max_length=100)),
                ('school', models.ForeignKey(to='schedule.School', related_name='school_email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='schoolemail',
            unique_together=set([('school', 'email_address')]),
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['day']},
        ),
    ]
