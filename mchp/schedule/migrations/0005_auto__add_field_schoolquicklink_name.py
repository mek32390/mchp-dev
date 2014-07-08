# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SchoolQuicklink.name'
        db.add_column('schedule_schoolquicklink', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=40, default='wat'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SchoolQuicklink.name'
        db.delete_column('schedule_schoolquicklink', 'name')


    models = {
        'schedule.course': {
            'Meta': {'unique_together': "(('domain', 'dept', 'course_number', 'professor'),)", 'object_name': 'Course'},
            'course_number': ('django.db.models.fields.IntegerField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'schedule.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'domain': ('django.db.models.fields.URLField', [], {'max_length': '200', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'schedule.schoolalias': {
            'Meta': {'unique_together': "(('domain', 'alias'),)", 'object_name': 'SchoolAlias'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']", 'related_name': "'SchoolAlias_domain'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'schedule.schoolquicklink': {
            'Meta': {'unique_together': "(('domain', 'quick_link'),)", 'object_name': 'SchoolQuicklink'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']", 'related_name': "'SchoolQuicklink_domain'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'quick_link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'schedule.section': {
            'Meta': {'unique_together': "(('domain', 'dept', 'course_number', 'professor', 'start_date', 'end_date'),)", 'object_name': 'Section'},
            'course_number': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.Course']", 'related_name': "'Section_course_number'"}),
            'dept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.Course']", 'related_name': "'Section_dept'"}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']", 'related_name': "'Section_domain'"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.Course']", 'related_name': "'Section_professor'"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['schedule']