# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'inboxes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificationArchive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('notification', models.ForeignKey(to='notification.Notification')),
                ('user', models.ForeignKey(related_name='notification_archive', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='inbox',
            name='notification',
            field=models.ForeignKey(to='notification.Notification'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inbox',
            name='user',
            field=models.ForeignKey(related_name='notification_inbox', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
