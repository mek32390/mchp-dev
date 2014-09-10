# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='schedule.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OneTimeEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, blank=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OneTimeFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(to='user_profile.OneTimeEvent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_points', models.IntegerField(default=0)),
                ('earned_points', models.IntegerField(default=0)),
                ('balance', models.DecimalField(default=Decimal('0.00'), decimal_places=4, max_digits=19)),
                ('kudos', models.IntegerField(default=0)),
                ('courses', models.ManyToManyField(to='schedule.Course', through='user_profile.Enrollment')),
                ('friends', models.ManyToManyField(to='user_profile.Student', db_table='user_profile_friends', related_name='friends_rel_+')),
                ('major', models.ForeignKey(to='schedule.Department', blank=True, null=True)),
                ('school', models.ForeignKey(related_name='student_school', to='schedule.School')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='student_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentQuicklink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quick_link', models.URLField()),
                ('name', models.CharField(max_length=40)),
                ('follows', models.ForeignKey(to='user_profile.StudentQuicklink', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL)),
                ('student', models.ForeignKey(related_name='userlink_student', to='user_profile.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='profile_pic/', blank=True, null=True)),
                ('blurb', models.CharField(blank=True, max_length=120)),
                ('student', models.OneToOneField(to='user_profile.Student', related_name='student_profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='user_roles')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='studentquicklink',
            unique_together=set([('student', 'quick_link')]),
        ),
        migrations.AddField(
            model_name='onetimeflag',
            name='student',
            field=models.ForeignKey(related_name='one_time_flag', to='user_profile.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(to='user_profile.Student'),
            preserve_default=True,
        ),
    ]
