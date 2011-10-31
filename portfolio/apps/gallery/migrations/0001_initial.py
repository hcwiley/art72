# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Piece'
        db.create_table('gallery_piece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=400)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['Piece'])

        # Adding model 'ExtendedImage'
        db.create_table('gallery_extendedimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('orig_file_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('piece', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Piece'])),
        ))
        db.send_create_signal('gallery', ['ExtendedImage'])


    def backwards(self, orm):
        
        # Deleting model 'Piece'
        db.delete_table('gallery_piece')

        # Deleting model 'ExtendedImage'
        db.delete_table('gallery_extendedimage')


    models = {
        'gallery.extendedimage': {
            'Meta': {'object_name': 'ExtendedImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'orig_file_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'piece': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Piece']"})
        },
        'gallery.piece': {
            'Meta': {'object_name': 'Piece'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '400'})
        }
    }

    complete_apps = ['gallery']
