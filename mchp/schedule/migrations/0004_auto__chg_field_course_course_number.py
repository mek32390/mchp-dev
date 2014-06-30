# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Course.course_number'
        db.execute(
            'ALTER TABLE "schedule_course" '
            'ALTER COLUMN "course_number" TYPE integer USING (trim(course_number)::integer)'
        )

    def backwards(self, orm):

        # Changing field 'Course.course_number'
        db.alter_column('schedule_course', 'course_number', self.gf('django.db.models.fields.CharField')(max_length=6))

    models = {
        'schedule.course': {
            'Meta': {'object_name': 'Course', 'unique_together': "(('domain', 'dept', 'course_number', 'professor'),)"},
            'course_number': ('django.db.models.fields.IntegerField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
        },
        'schedule.schoolalias': {
            'Meta': {'object_name': 'SchoolAlias', 'unique_together': "(('domain', 'alias'),)"},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']", 'related_name': "'SchoolAlias_domain'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'schedule.schoolquicklink': {
            'Meta': {'object_name': 'SchoolQuicklink', 'unique_together': "(('domain', 'quick_link'),)"},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']", 'related_name': "'SchoolQuicklink_domain'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quick_link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'schedule.section': {
            'Meta': {'object_name': 'Section', 'unique_together': "(('domain', 'dept', 'course_number', 'professor', 'start_date', 'end_date'),)"},
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
