# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Theme.top_level_css'
        db.add_column('gallery_theme', 'top_level_css', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='gallery_theme_top_level_css', to=orm['gallery.CssFileWrapper']), keep_default=False)

        # Adding field 'Theme.color_css'
        db.add_column('gallery_theme', 'color_css', self.gf('django.db.models.fields.related.ForeignKey')(default=2, related_name='gallery_theme_color_css', to=orm['gallery.CssFileWrapper']), keep_default=False)

        # Adding field 'Theme.font_css'
        db.add_column('gallery_theme', 'font_css', self.gf('django.db.models.fields.related.ForeignKey')(default=2, related_name='gallery_theme_font_css', to=orm['gallery.CssFileWrapper']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Theme.top_level_css'
        db.delete_column('gallery_theme', 'top_level_css_id')

        # Deleting field 'Theme.color_css'
        db.delete_column('gallery_theme', 'color_css_id')

        # Deleting field 'Theme.font_css'
        db.delete_column('gallery_theme', 'font_css_id')


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
        'gallery.cssfilewrapper': {
            'Meta': {'object_name': 'CssFileWrapper'},
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
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
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'color_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_color_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'font_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_font_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'top_level_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_top_level_css'", 'to': "orm['gallery.CssFileWrapper']"})
        }
    }

    complete_apps = ['gallery']
