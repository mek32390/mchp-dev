# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20140923_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolemail',
            old_name='email_address',
            new_name='email_domain',
        ),
        migrations.AlterUniqueTogether(
            name='schoolemail',
            unique_together=set([('school', 'email_domain')]),
        ),
    ]
