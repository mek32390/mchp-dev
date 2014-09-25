# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20140925_0029'),
        ('schedule', '0007_auto_20140923_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='schedule.Course')),
                ('student', models.ForeignKey(to='user_profile.Student', related_name='courses')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
