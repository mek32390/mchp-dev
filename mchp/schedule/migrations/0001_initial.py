# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import schedule.utils
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('dept', models.CharField(max_length=6)),
                ('course_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(99)])),
                ('name', models.CharField(max_length=13)),
                ('professor', models.CharField(max_length=30)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('domain', models.URLField(validators=[schedule.utils.clean_domain])),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=60)),
                ('city', models.CharField(blank=True, max_length=60)),
                ('state', models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('AS', 'American Samoa'), ('GU', 'Guam'), ('MP', 'Northern Mariana Islands'), ('PR', 'Puerto Rico'), ('VI', 'Virgin Islands')], max_length=20)),
                ('country', models.CharField(blank=True, max_length=45)),
                ('zip_code', models.CharField(blank=True, max_length=11)),
                ('timezone', models.CharField(blank=True, max_length=50)),
                ('lat', models.DecimalField(decimal_places=15, max_digits=19, default=Decimal('0.000'))),
                ('lng', models.DecimalField(decimal_places=15, max_digits=19, default=Decimal('0.000'))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SchoolAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('alias', models.CharField(max_length=100)),
                ('domain', models.ForeignKey(related_name='SchoolAlias_domain', to='schedule.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SchoolQuicklink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quick_link', models.URLField()),
                ('name', models.CharField(max_length=40)),
                ('domain', models.ForeignKey(related_name='SchoolQuicklink_domain', to='schedule.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('day', models.PositiveSmallIntegerField(choices=[(0, 'Mon'), (1, 'Tues'), (2, 'Wed'), (3, 'Thur'), (4, 'Fri'), (5, 'Sat')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course', models.ForeignKey(related_name='sections', to='schedule.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='schoolquicklink',
            unique_together=set([('domain', 'quick_link')]),
        ),
        migrations.AlterUniqueTogether(
            name='schoolalias',
            unique_together=set([('domain', 'alias')]),
        ),
        migrations.AddField(
            model_name='course',
            name='domain',
            field=models.ForeignKey(to='schedule.School'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('domain', 'dept', 'course_number', 'professor')]),
        ),
    ]
