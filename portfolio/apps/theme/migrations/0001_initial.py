# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ColorPalette'
        db.create_table('theme_colorpalette', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('c1', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('c2', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('c3', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('c4', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('c5', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal('theme', ['ColorPalette'])

        # Adding model 'TypeKitFont'
        db.create_table('theme_typekitfont', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('typekit', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('theme', ['TypeKitFont'])

        # Adding model 'FontPair'
        db.create_table('theme_fontpair', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('f1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_fontpair_f1', to=orm['theme.TypeKitFont'])),
            ('f2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_fontpair_f2', to=orm['theme.TypeKitFont'])),
        ))
        db.send_create_signal('theme', ['FontPair'])

        # Adding unique constraint on 'FontPair', fields ['f1', 'f2']
        db.create_unique('theme_fontpair', ['f1_id', 'f2_id'])

        # Adding model 'Layout'
        db.create_table('theme_layout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('depth', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('css_template', self.gf('django.db.models.fields.TextField')()),
            ('icon', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image_dimension', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('thumb_dimension', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('supports_background_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('theme', ['Layout'])

        # Adding model 'Theme'
        db.create_table('theme_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('colors', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theme.ColorPalette'])),
            ('fonts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theme.FontPair'])),
            ('depth', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('site_layout', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_site_layout', to=orm['theme.Layout'])),
            ('piece_layout', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_theme_piece_layout', to=orm['theme.Layout'])),
            ('series_layout', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='theme_theme_series_layout', null=True, to=orm['theme.Layout'])),
            ('category_layout', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='theme_theme_category_layout', null=True, to=orm['theme.Layout'])),
            ('background_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('theme', ['Theme'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'FontPair', fields ['f1', 'f2']
        db.delete_unique('theme_fontpair', ['f1_id', 'f2_id'])

        # Deleting model 'ColorPalette'
        db.delete_table('theme_colorpalette')

        # Deleting model 'TypeKitFont'
        db.delete_table('theme_typekitfont')

        # Deleting model 'FontPair'
        db.delete_table('theme_fontpair')

        # Deleting model 'Layout'
        db.delete_table('theme_layout')

        # Deleting model 'Theme'
        db.delete_table('theme_theme')


    models = {
        'theme.colorpalette': {
            'Meta': {'object_name': 'ColorPalette'},
            'c1': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'c2': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'c3': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'c4': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'c5': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'theme.fontpair': {
            'Meta': {'unique_together': "(('f1', 'f2'),)", 'object_name': 'FontPair'},
            'f1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_fontpair_f1'", 'to': "orm['theme.TypeKitFont']"}),
            'f2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_fontpair_f2'", 'to': "orm['theme.TypeKitFont']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'theme.layout': {
            'Meta': {'object_name': 'Layout'},
            'css_template': ('django.db.models.fields.TextField', [], {}),
            'depth': ('django.db.models.fields.SmallIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_dimension': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'supports_background_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thumb_dimension': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'theme.theme': {
            'Meta': {'object_name': 'Theme'},
            'background_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category_layout': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'theme_theme_category_layout'", 'null': 'True', 'to': "orm['theme.Layout']"}),
            'colors': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['theme.ColorPalette']"}),
            'depth': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fonts': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['theme.FontPair']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piece_layout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_piece_layout'", 'to': "orm['theme.Layout']"}),
            'series_layout': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'theme_theme_series_layout'", 'null': 'True', 'to': "orm['theme.Layout']"}),
            'site_layout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_theme_site_layout'", 'to': "orm['theme.Layout']"})
        },
        'theme.typekitfont': {
            'Meta': {'object_name': 'TypeKitFont'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'typekit': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['theme']
