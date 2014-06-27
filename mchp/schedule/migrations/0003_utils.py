# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table('schedule_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('schedule', ['Section'])

        # Adding unique constraint on 'Course', fields ['domain', 'dept', 'course_number', 'professor']
        db.create_unique('schedule_course', ['domain_id', 'dept', 'course_number', 'professor'])


    def backwards(self, orm):
        # Removing unique constraint on 'Course', fields ['domain', 'dept', 'course_number', 'professor']
        db.delete_unique('schedule_course', ['domain_id', 'dept', 'course_number', 'professor'])

        # Deleting model 'Section'
        db.delete_table('schedule_section')


    models = {
        'schedule.course': {
            'Meta': {'unique_together': "(('domain', 'dept', 'course_number', 'professor'),)", 'object_name': 'Course'},
            'course_number': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'schedule.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'domain': ('django.db.models.fields.URLField', [], {'primary_key': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'schedule.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['schedule']