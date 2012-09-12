# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table('artist_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('statement', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resume', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('theme', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['theme.Theme'], unique=True, null=True, blank=True)),
            ('vimeo_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('artist', ['Artist'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table('artist_artist')


    models = {
        'artist.artist': {
            'Meta': {'object_name': 'Artist'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'statement': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'theme': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['theme.Theme']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'vimeo_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'typekit': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['artist']