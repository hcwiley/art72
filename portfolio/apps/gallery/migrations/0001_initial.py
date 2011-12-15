# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('gallery_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'])),
        ))
        db.send_create_signal('gallery', ['Category'])

        # Adding unique constraint on 'Category', fields ['name', 'artist']
        db.create_unique('gallery_category', ['name', 'artist_id'])

        # Adding model 'Series'
        db.create_table('gallery_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Category'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['Series'])

        # Adding model 'Piece'
        db.create_table('gallery_piece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Series'], null=True, blank=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'])),
        ))
        db.send_create_signal('gallery', ['Piece'])

        # Adding model 'ExtendedImage'
        db.create_table('gallery_extendedimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('orig_file_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('piece', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Piece'])),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'])),
        ))
        db.send_create_signal('gallery', ['ExtendedImage'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Category', fields ['name', 'artist']
        db.delete_unique('gallery_category', ['name', 'artist_id'])

        # Deleting model 'Category'
        db.delete_table('gallery_category')

        # Deleting model 'Series'
        db.delete_table('gallery_series')

        # Deleting model 'Piece'
        db.delete_table('gallery_piece')

        # Deleting model 'ExtendedImage'
        db.delete_table('gallery_extendedimage')


    models = {
        'artist.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'statement': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'gallery.category': {
            'Meta': {'unique_together': "(('name', 'artist'),)", 'object_name': 'Category'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gallery.extendedimage': {
            'Meta': {'object_name': 'ExtendedImage'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'orig_file_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'piece': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Piece']"})
        },
        'gallery.piece': {
            'Meta': {'object_name': 'Piece'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Artist']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Series']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'gallery.series': {
            'Meta': {'object_name': 'Series'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Artist']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['gallery']
