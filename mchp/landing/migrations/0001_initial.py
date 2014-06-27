# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageHit'
        db.create_table('landing_pagehit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agent', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('landing', ['PageHit'])


    def backwards(self, orm):
        # Deleting model 'PageHit'
        db.delete_table('landing_pagehit')


    models = {
        'landing.pagehit': {
            'Meta': {'object_name': 'PageHit'},
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['landing']