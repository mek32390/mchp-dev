# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('stripe_id', models.CharField(max_length=100)),
                ('recipient_id', models.CharField(max_length=100, null=True, blank=True)),
                ('default', models.BooleanField(default=False)),
                ('last_four', models.CharField(max_length=4)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='stripe', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebhookMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('message', jsonfield.fields.JSONField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='stripecustomer',
            unique_together=set([('user', 'stripe_id')]),
        ),
    ]
