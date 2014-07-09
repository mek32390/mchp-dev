# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Upload'
        db.create_table('documents_upload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Document'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profile.Student'])),
        ))
        db.send_create_signal('documents', ['Upload'])

        # Adding unique constraint on 'Upload', fields ['document', 'owner']
        db.create_unique('documents_upload', ['document_id', 'owner_id'])

        # Adding model 'Purchased'
        db.create_table('documents_purchased', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purchased_document', to=orm['documents.Document'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profile.Student'])),
        ))
        db.send_create_signal('documents', ['Purchased'])

        # Adding unique constraint on 'Purchased', fields ['document', 'student']
        db.create_unique('documents_purchased', ['document_id', 'student_id'])

        # Deleting field 'Document.rating'
        db.delete_column('documents_document', 'rating')

        # Deleting field 'Document.purchased'
        db.delete_column('documents_document', 'purchased')

        # Adding field 'Document.up'
        db.add_column('documents_document', 'up',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Document.down'
        db.add_column('documents_document', 'down',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Document.md5sum'
        db.add_column('documents_document', 'md5sum',
                      self.gf('django.db.models.fields.CharField')(max_length=32, default=4),
                      keep_default=False)

        # Adding field 'Document.uuid'
        db.add_column('documents_document', 'uuid',
                      self.gf('django.db.models.fields.CharField')(max_length=32, default=8),
                      keep_default=False)


        # Changing field 'Document.price'
        db.alter_column('documents_document', 'price', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Document.title'
        db.alter_column('documents_document', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Document.slug'
        db.alter_column('documents_document', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=80))

    def backwards(self, orm):
        # Removing unique constraint on 'Purchased', fields ['document', 'student']
        db.delete_unique('documents_purchased', ['document_id', 'student_id'])

        # Removing unique constraint on 'Upload', fields ['document', 'owner']
        db.delete_unique('documents_upload', ['document_id', 'owner_id'])

        # Deleting model 'Upload'
        db.delete_table('documents_upload')

        # Deleting model 'Purchased'
        db.delete_table('documents_purchased')

        # Adding field 'Document.rating'
        db.add_column('documents_document', 'rating',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Document.purchased'
        db.add_column('documents_document', 'purchased',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Document.up'
        db.delete_column('documents_document', 'up')

        # Deleting field 'Document.down'
        db.delete_column('documents_document', 'down')

        # Deleting field 'Document.md5sum'
        db.delete_column('documents_document', 'md5sum')

        # Deleting field 'Document.uuid'
        db.delete_column('documents_document', 'uuid')


        # Changing field 'Document.price'
        db.alter_column('documents_document', 'price', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=5))

        # Changing field 'Document.title'
        db.alter_column('documents_document', 'title', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Document.slug'
        db.alter_column('documents_document', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=60))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
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
        'documents.purchased': {
            'Meta': {'object_name': 'Purchased', 'unique_together': "(('document', 'student'),)"},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchased_document'", 'to': "orm['documents.Document']"}),
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
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'db_table': "'user_profile_enrollment'", 'symmetrical': 'False', 'to': "orm['schedule.Course']"}),
            'earned_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kudos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'purchased_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_school'", 'to': "orm['schedule.School']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'student_user'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'work_credit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['documents']