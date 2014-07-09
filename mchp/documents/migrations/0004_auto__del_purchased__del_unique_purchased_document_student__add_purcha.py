# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Purchased', fields ['document', 'student']
        db.delete_unique('documents_purchased', ['document_id', 'student_id'])

        # Deleting model 'Purchased'
        db.delete_table('documents_purchased')

        # Adding model 'DocumentPurchase'
        db.create_table('documents_documentpurchase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Document'], related_name='purchased_document')),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profile.Student'])),
        ))
        db.send_create_signal('documents', ['DocumentPurchase'])

        # Adding unique constraint on 'DocumentPurchase', fields ['document', 'student']
        db.create_unique('documents_documentpurchase', ['document_id', 'student_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'DocumentPurchase', fields ['document', 'student']
        db.delete_unique('documents_documentpurchase', ['document_id', 'student_id'])

        # Adding model 'Purchased'
        db.create_table('documents_purchased', (
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profile.Student'])),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Document'], related_name='purchased_document')),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('documents', ['Purchased'])

        # Adding unique constraint on 'Purchased', fields ['document', 'student']
        db.create_unique('documents_purchased', ['document_id', 'student_id'])

        # Deleting model 'DocumentPurchase'
        db.delete_table('documents_documentpurchase')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'documents.document': {
            'Meta': {'object_name': 'Document'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'down': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'md5sum': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '80'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'up': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'documents.documentpurchase': {
            'Meta': {'object_name': 'DocumentPurchase', 'unique_together': "(('document', 'student'),)"},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.Document']", 'related_name': "'purchased_document'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profile.Student']"})
        },
        'documents.upload': {
            'Meta': {'object_name': 'Upload', 'unique_together': "(('document', 'owner'),)"},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profile.Student']"})
        },
        'schedule.course': {
            'Meta': {'object_name': 'Course', 'unique_together': "(('domain', 'dept', 'course_number', 'professor'),)"},
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
            'domain': ('django.db.models.fields.URLField', [], {'max_length': '200', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'})
        },
        'user_profile.student': {
            'Meta': {'object_name': 'Student'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'db_table': "'user_profile_enrollment'", 'to': "orm['schedule.Course']"}),
            'earned_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kudos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'purchased_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schedule.School']", 'related_name': "'student_school'"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']", 'related_name': "'student_user'"}),
            'work_credit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['documents']