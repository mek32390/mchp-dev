# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'School.street'
        db.delete_column('schedule_school', 'street')

        # Adding field 'School.address'
        db.add_column('schedule_school', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', blank=True, max_length=60),
                      keep_default=False)


        # Changing field 'School.city'
        db.alter_column('schedule_school', 'city', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'School.country'
        db.alter_column('schedule_school', 'country', self.gf('django.db.models.fields.CharField')(max_length=45))

        # Changing field 'School.name'
        db.alter_column('schedule_school', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))
        # Adding field 'SchoolQuicklink.name'
        db.add_column('schedule_schoolquicklink', 'name',
                      self.gf('django.db.models.fields.CharField')(default='wat', max_length=40),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'School.street'
        db.add_column('schedule_school', 'street',
                      self.gf('django.db.models.fields.CharField')(default='', blank=True, max_length=30),
                      keep_default=False)

        # Deleting field 'School.address'
        db.delete_column('schedule_school', 'address')


        # Changing field 'School.city'
        db.alter_column('schedule_school', 'city', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'School.country'
        db.alter_column('schedule_school', 'country', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'School.name'
        db.alter_column('schedule_school', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))
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
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '45'}),
            'domain': ('django.db.models.fields.URLField', [], {'primary_key': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'})
        },
        'schedule.schoolalias': {
            'Meta': {'unique_together': "(('domain', 'alias'),)", 'object_name': 'SchoolAlias'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SchoolAlias_domain'", 'to': "orm['schedule.School']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'schedule.schoolquicklink': {
            'Meta': {'unique_together': "(('domain', 'quick_link'),)", 'object_name': 'SchoolQuicklink'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SchoolQuicklink_domain'", 'to': "orm['schedule.School']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'quick_link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'schedule.section': {
            'Meta': {'unique_together': "(('domain', 'dept', 'course_number', 'professor', 'start_date', 'end_date'),)", 'object_name': 'Section'},
            'course_number': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Section_course_number'", 'to': "orm['schedule.Course']"}),
            'dept': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Section_dept'", 'to': "orm['schedule.Course']"}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Section_domain'", 'to': "orm['schedule.School']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Section_professor'", 'to': "orm['schedule.Course']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['schedule']