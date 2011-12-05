# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Theme.site_css'
        db.add_column('gallery_theme', 'site_css', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='gallery_theme_site_css', to=orm['gallery.CssFileWrapper']), keep_default=False)

        # Adding field 'Theme.index_css'
        db.add_column('gallery_theme', 'index_css', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='gallery_theme_index_css', to=orm['gallery.CssFileWrapper']), keep_default=False)

        # Adding field 'Theme.contact_css'
        db.add_column('gallery_theme', 'contact_css', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='gallery_theme_contact_css', to=orm['gallery.CssFileWrapper']), keep_default=False)

        # Adding field 'Theme.category_css'
        db.add_column('gallery_theme', 'category_css', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='gallery_theme_category_css', to=orm['gallery.CssFileWrapper']), keep_default=False)

        # Adding field 'Theme.series_css'
        db.add_column('gallery_theme', 'series_css', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='gallery_theme_series_css', to=orm['gallery.CssFileWrapper']), keep_default=False)

        # Adding field 'Theme.piece_css'
        db.add_column('gallery_theme', 'piece_css', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='gallery_theme_piece_css', to=orm['gallery.CssFileWrapper']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Theme.site_css'
        db.delete_column('gallery_theme', 'site_css_id')

        # Deleting field 'Theme.index_css'
        db.delete_column('gallery_theme', 'index_css_id')

        # Deleting field 'Theme.contact_css'
        db.delete_column('gallery_theme', 'contact_css_id')

        # Deleting field 'Theme.category_css'
        db.delete_column('gallery_theme', 'category_css_id')

        # Deleting field 'Theme.series_css'
        db.delete_column('gallery_theme', 'series_css_id')

        # Deleting field 'Theme.piece_css'
        db.delete_column('gallery_theme', 'piece_css_id')


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
            'category_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_category_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'color_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_color_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'contact_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_contact_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'font_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_font_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_index_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'piece_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_piece_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'series_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_series_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'site_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_site_css'", 'to': "orm['gallery.CssFileWrapper']"}),
            'top_level_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gallery_theme_top_level_css'", 'to': "orm['gallery.CssFileWrapper']"})
        }
    }

    complete_apps = ['gallery']
