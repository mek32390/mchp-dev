# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('user_profile_userprofile')

        # Adding model 'Student'
        db.create_table('user_profile_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='student_user', to=orm['auth.User'], unique=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(related_name='student_school', to=orm['schedule.School'])),
            ('purchased_points', self.gf('django.db.models.fields.IntegerField')()),
            ('earned_points', self.gf('django.db.models.fields.IntegerField')()),
            ('kudos', self.gf('django.db.models.fields.IntegerField')()),
            ('work_credit', self.gf('django.db.models.fields.IntegerField')()),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('user_profile', ['Student'])


    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('user_profile_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], related_name='profile', unique=True)),
        ))
        db.send_create_signal('user_profile', ['UserProfile'])

        # Deleting model 'Student'
        db.delete_table('user_profile_student')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        'user_profile.student': {
            'Meta': {'object_name': 'Student'},
            'earned_points': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kudos': ('django.db.models.fields.IntegerField', [], {}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'purchased_points': ('django.db.models.fields.IntegerField', [], {}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_school'", 'to': "orm['schedule.School']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'student_user'", 'to': "orm['auth.User']", 'unique': 'True'}),
            'work_credit': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['user_profile']