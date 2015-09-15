# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_merge'),
        ('documents', '0008_auto_20150909_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(null=True, to='user_profile.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='roster',
            field=models.ForeignKey(to='rosters.Roster', blank=True, null=True, related_name='syllabus'),
        ),
        migrations.RunSQL(
            'UPDATE documents_document SET owner_id = (SELECT owner_id FROM documents_upload where documents_upload.document_id = documents_document.id)'
        ),
        migrations.AlterUniqueTogether(
            name='upload',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='upload',
            name='document',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Upload',
        )
    ]
