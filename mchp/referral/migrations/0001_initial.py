# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('user', models.ForeignKey(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False, related_name='referree')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferralCode',
            fields=[
                ('user', models.ForeignKey(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False, related_name='referal_code')),
                ('referral_code', models.CharField(unique=True, max_length=13)),
                ('referral_link', models.CharField(unique=True, max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='referral',
            name='referrer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='referrer'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='referral',
            unique_together=set([('user', 'referrer')]),
        ),
    ]
