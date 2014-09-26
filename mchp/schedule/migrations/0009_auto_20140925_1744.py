# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_enrollment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['dept', 'course_number', 'professor']},
        ),
        migrations.AddField(
            model_name='enrollment',
            name='receive_email',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(to='user_profile.Student', related_name='enrollment'),
        ),
    ]
