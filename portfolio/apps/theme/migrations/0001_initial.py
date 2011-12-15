# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CssFileWrapper'
        db.create_table('theme_cssfilewrapper', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('blurb', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('theme', ['CssFileWrapper'])

        # Adding model 'Theme'
        db.create_table('theme_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('site_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_site_css', to=orm['theme.CssFileWrapper'])),
            ('index_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_index_css', to=orm['theme.CssFileWrapper'])),
            ('contact_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_contact_css', to=orm['theme.CssFileWrapper'])),
            ('top_level_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_top_level_css', to=orm['theme.CssFileWrapper'])),
            ('category_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_category_css', to=orm['theme.CssFileWrapper'])),
            ('series_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_series_css', to=orm['theme.CssFileWrapper'])),
            ('piece_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_piece_css', to=orm['theme.CssFileWrapper'])),
            ('color_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_color_css', to=orm['theme.CssFileWrapper'])),
            ('font_css', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_font_css', to=orm['theme.CssFileWrapper'])),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'])),
        ))
        db.send_create_signal('theme', ['Theme'])


    def backwards(self, orm):
        
        # Deleting model 'CssFileWrapper'
        db.delete_table('theme_cssfilewrapper')

        # Deleting model 'Theme'
        db.delete_table('theme_theme')


    models = {
        'artist.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'statement': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'theme.cssfilewrapper': {
            'Meta': {'object_name': 'CssFileWrapper'},
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'theme.theme': {
            'Meta': {'object_name': 'Theme'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Artist']"}),
            'category_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_category_css'", 'to': "orm['theme.CssFileWrapper']"}),
            'color_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_color_css'", 'to': "orm['theme.CssFileWrapper']"}),
            'contact_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_contact_css'", 'to': "orm['theme.CssFileWrapper']"}),
            'font_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_font_css'", 'to': "orm['theme.CssFileWrapper']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_index_css'", 'to': "orm['theme.CssFileWrapper']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'piece_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_piece_css'", 'to': "orm['theme.CssFileWrapper']"}),
            'series_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_series_css'", 'to': "orm['theme.CssFileWrapper']"}),
            'site_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_site_css'", 'to': "orm['theme.CssFileWrapper']"}),
            'top_level_css': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_top_level_css'", 'to': "orm['theme.CssFileWrapper']"})
        }
    }

    complete_apps = ['theme']
