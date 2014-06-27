# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SchoolAlias'
        db.create_table('schedule_schoolalias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(related_name='SchoolAlias_domain', to=orm['schedule.School'])),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal('schedule', ['SchoolAlias'])

        # Adding unique constraint on 'SchoolAlias', fields ['domain', 'alias']
        db.create_unique('schedule_schoolalias', ['domain_id', 'alias'])

        # Adding model 'SchoolQuicklink'
        db.create_table('schedule_schoolquicklink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(related_name='SchoolQuicklink_domain', to=orm['schedule.School'])),
            ('quick_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('schedule', ['SchoolQuicklink'])

        # Adding unique constraint on 'SchoolQuicklink', fields ['domain', 'quick_link']
        db.create_unique('schedule_schoolquicklink', ['domain_id', 'quick_link'])

        # Adding model 'Section'
        db.create_table('schedule_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Section_domain', to=orm['schedule.School'])),
            ('dept', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Section_dept', to=orm['schedule.Course'])),
            ('course_number', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Section_course_number', to=orm['schedule.Course'])),
            ('professor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Section_professor', to=orm['schedule.Course'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('schedule', ['Section'])

        # Adding unique constraint on 'Section', fields ['domain', 'dept', 'course_number', 'professor', 'start_date', 'end_date']
        db.create_unique('schedule_section', ['domain_id', 'dept_id', 'course_number_id', 'professor_id', 'start_date', 'end_date'])

        # Adding unique constraint on 'Course', fields ['domain', 'dept', 'course_number', 'professor']
        db.create_unique('schedule_course', ['domain_id', 'dept', 'course_number', 'professor'])


    def backwards(self, orm):
        # Removing unique constraint on 'Course', fields ['domain', 'dept', 'course_number', 'professor']
        db.delete_unique('schedule_course', ['domain_id', 'dept', 'course_number', 'professor'])

        # Removing unique constraint on 'Section', fields ['domain', 'dept', 'course_number', 'professor', 'start_date', 'end_date']
        db.delete_unique('schedule_section', ['domain_id', 'dept_id', 'course_number_id', 'professor_id', 'start_date', 'end_date'])

        # Removing unique constraint on 'SchoolQuicklink', fields ['domain', 'quick_link']
        db.delete_unique('schedule_schoolquicklink', ['domain_id', 'quick_link'])

        # Removing unique constraint on 'SchoolAlias', fields ['domain', 'alias']
        db.delete_unique('schedule_schoolalias', ['domain_id', 'alias'])

        # Deleting model 'SchoolAlias'
        db.delete_table('schedule_schoolalias')

        # Deleting model 'SchoolQuicklink'
        db.delete_table('schedule_schoolquicklink')

        # Deleting model 'Section'
        db.delete_table('schedule_section')


    models = {
        'schedule.course': {
            'Meta': {'object_name': 'Course', 'unique_together': "(('domain', 'dept', 'course_number', 'professor'),)"},
            'course_number': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
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
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SchoolAlias_domain'", 'to': "orm['schedule.School']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'schedule.schoolquicklink': {
            'Meta': {'object_name': 'SchoolQuicklink', 'unique_together': "(('domain', 'quick_link'),)"},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SchoolQuicklink_domain'", 'to': "orm['schedule.School']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quick_link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'schedule.section': {
            'Meta': {'object_name': 'Section', 'unique_together': "(('domain', 'dept', 'course_number', 'professor', 'start_date', 'end_date'),)"},
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