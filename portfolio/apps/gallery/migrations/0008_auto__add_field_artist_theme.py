# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Artist.theme'
        db.add_column('gallery_artist', 'theme', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Theme']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Artist.theme'
        db.delete_column('gallery_artist', 'theme_id')


    models = {
        'gallery.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Theme']"})
        },
        'gallery.category': {
            'Meta': {'object_name': 'Category'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'gallery.colorpalette': {
            'Meta': {'object_name': 'ColorPalette'},
            'c1': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'c2': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'c3': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'c4': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'c5': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'c6': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'gallery.extendedimage': {
            'Meta': {'object_name': 'ExtendedImage'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'orig_file_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'piece': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Piece']"})
        },
        'gallery.piece': {
            'Meta': {'object_name': 'Piece'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Series']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '400'})
        },
        'gallery.series': {
            'Meta': {'object_name': 'Series'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '400'})
        },
        'gallery.theme': {
            'Meta': {'object_name': 'Theme'},
            'colors': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.ColorPalette']"}),
            'css': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['gallery']
