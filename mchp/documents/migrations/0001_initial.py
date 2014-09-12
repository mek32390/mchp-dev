# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('schedule', '0002_section_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('up', models.IntegerField(default=0)),
                ('down', models.IntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('document', models.FileField(upload_to='documents/')),
                ('filetype', models.CharField(max_length=150)),
                ('md5sum', models.CharField(max_length=32)),
                ('uuid', models.CharField(max_length=32)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('preview', models.ImageField(null=True, blank=True, upload_to='previews/')),
                ('slug', models.SlugField(max_length=80)),
                ('course', models.ForeignKey(to='schedule.Course', on_delete=models.SET(documents.models.get_sentinel_course))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocumentFlag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('status', models.PositiveIntegerField(default=1, choices=[(1, 'Flagged'), (2, 'Under review'), (3, 'Ticket closed'), (4, 'Content removed')])),
                ('reason', models.PositiveSmallIntegerField(choices=[(1, 'Instructor notes'), (2, 'Duplication Document'), (3, 'Other reason')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('closed', models.DateTimeField(null=True, blank=True)),
                ('ip', models.IPAddressField(null=True, blank=True)),
                ('detail', models.CharField(max_length=300, blank=True)),
                ('staff_comment', models.TextField(null=True, blank=True)),
                ('document', models.ForeignKey(to='documents.Document', related_name='flags')),
                ('student', models.ForeignKey(to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocumentPurchase',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('review', models.CharField(max_length=250, blank=True)),
                ('review_date', models.DateTimeField(null=True, blank=True)),
                ('document', models.ForeignKey(to='documents.Document', related_name='purchased_document')),
                ('student', models.ForeignKey(to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('document', models.OneToOneField(to='documents.Document')),
                ('owner', models.ForeignKey(to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='upload',
            unique_together=set([('document', 'owner')]),
        ),
        migrations.AlterUniqueTogether(
            name='documentpurchase',
            unique_together=set([('document', 'student')]),
        ),
    ]
