# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Category.artist'
        db.add_column('gallery_category', 'artist', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Artist']), keep_default=False)

        # Adding field 'Series.artist'
        db.add_column('gallery_series', 'artist', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Artist']), keep_default=False)

        # Adding field 'Piece.artist'
        db.add_column('gallery_piece', 'artist', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Artist']), keep_default=False)

        # Adding field 'ExtendedImage.artist'
        db.add_column('gallery_extendedimage', 'artist', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Artist']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Category.artist'
        db.delete_column('gallery_category', 'artist_id')

        # Deleting field 'Series.artist'
        db.delete_column('gallery_series', 'artist_id')

        # Deleting field 'Piece.artist'
        db.delete_column('gallery_piece', 'artist_id')

        # Deleting field 'ExtendedImage.artist'
        db.delete_column('gallery_extendedimage', 'artist_id')


    models = {
        'gallery.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gallery.category': {
            'Meta': {'object_name': 'Category'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
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
        }
    }

    complete_apps = ['gallery']
