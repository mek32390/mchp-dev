# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table('schedule_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.School'])),
            ('dept', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('course_number', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('professor', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('schedule', ['Course'])

        # Adding model 'School'
        db.create_table('schedule_school', (
            ('domain', self.gf('django.db.models.fields.URLField')(primary_key=True, max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20)),
            ('street', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, max_length=25)),
        ))
        db.send_create_signal('schedule', ['School'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table('schedule_course')

        # Deleting model 'School'
        db.delete_table('schedule_school')


    models = {
        'schedule.course': {
            'Meta': {'object_name': 'Course'},
            'course_number': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'schedule.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '25'}),
            'domain': ('django.db.models.fields.URLField', [], {'primary_key': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'street': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['schedule']