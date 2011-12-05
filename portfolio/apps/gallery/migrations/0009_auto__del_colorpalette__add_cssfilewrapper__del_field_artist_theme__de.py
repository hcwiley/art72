# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ColorPalette'
        db.delete_table('gallery_colorpalette')

        # Adding model 'CssFileWrapper'
        db.create_table('gallery_cssfilewrapper', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('blurb', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('gallery', ['CssFileWrapper'])

        # Deleting field 'Artist.theme'
        db.delete_column('gallery_artist', 'theme_id')

        # Deleting field 'Theme.colors'
        db.delete_column('gallery_theme', 'colors_id')

        # Deleting field 'Theme.css'
        db.delete_column('gallery_theme', 'css')

        # Adding field 'Theme.artist'
        db.add_column('gallery_theme', 'artist', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Artist']), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'ColorPalette'
        db.create_table('gallery_colorpalette', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('c3', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('c2', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('c1', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('c6', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('c5', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('c4', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('gallery', ['ColorPalette'])

        # Deleting model 'CssFileWrapper'
        db.delete_table('gallery_cssfilewrapper')

        # User chose to not deal with backwards NULL issues for 'Artist.theme'
        raise RuntimeError("Cannot reverse this migration. 'Artist.theme' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Theme.colors'
        raise RuntimeError("Cannot reverse this migration. 'Theme.colors' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Theme.css'
        raise RuntimeError("Cannot reverse this migration. 'Theme.css' and its values cannot be restored.")

        # Deleting field 'Theme.artist'
        db.delete_column('gallery_theme', 'artist_id')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['gallery']
