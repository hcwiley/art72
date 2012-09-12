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
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['artist.Artist'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('preferred_child', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gallery_category_preferred_child', null=True, to=orm['gallery.Series'])),
        ))
        db.send_create_signal('gallery', ['Category'])

        # Adding unique constraint on 'Category', fields ['slug', 'artist']
        db.create_unique('gallery_category', ['slug', 'artist_id'])

        # Adding unique constraint on 'Category', fields ['title', 'artist']
        db.create_unique('gallery_category', ['title', 'artist_id'])

        # Adding model 'Series'
        db.create_table('gallery_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['artist.Artist'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Category'], null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('preferred_child', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gallery_series_preferred_child', null=True, to=orm['gallery.Piece'])),
        ))
        db.send_create_signal('gallery', ['Series'])

        # Adding unique constraint on 'Series', fields ['slug', 'artist']
        db.create_unique('gallery_series', ['slug', 'artist_id'])

        # Adding model 'Piece'
        db.create_table('gallery_piece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['artist.Artist'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('materials', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('dimensions', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Series'], null=True, blank=True)),
            ('for_sale', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('preferred_child', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gallery_piece_preferred_child', null=True, to=orm['gallery.ExtendedMedia'])),
        ))
        db.send_create_signal('gallery', ['Piece'])

        # Adding unique constraint on 'Piece', fields ['slug', 'artist']
        db.create_unique('gallery_piece', ['slug', 'artist_id'])

        # Adding model 'ExtendedMedia'
        db.create_table('gallery_extendedmedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['artist.Artist'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('piece', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Piece'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('media_type', self.gf('django.db.models.fields.SmallIntegerField')(max_length=20)),
            ('api_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['ExtendedMedia'])

        # Adding unique constraint on 'ExtendedMedia', fields ['slug', 'artist']
        db.create_unique('gallery_extendedmedia', ['slug', 'artist_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'ExtendedMedia', fields ['slug', 'artist']
        db.delete_unique('gallery_extendedmedia', ['slug', 'artist_id'])

        # Removing unique constraint on 'Piece', fields ['slug', 'artist']
        db.delete_unique('gallery_piece', ['slug', 'artist_id'])

        # Removing unique constraint on 'Series', fields ['slug', 'artist']
        db.delete_unique('gallery_series', ['slug', 'artist_id'])

        # Removing unique constraint on 'Category', fields ['title', 'artist']
        db.delete_unique('gallery_category', ['title', 'artist_id'])

        # Removing unique constraint on 'Category', fields ['slug', 'artist']
        db.delete_unique('gallery_category', ['slug', 'artist_id'])

        # Deleting model 'Category'
        db.delete_table('gallery_category')

        # Deleting model 'Series'
        db.delete_table('gallery_series')

        # Deleting model 'Piece'
        db.delete_table('gallery_piece')

        # Deleting model 'ExtendedMedia'
        db.delete_table('gallery_extendedmedia')


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
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 11, 21, 25, 26, 782587)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 11, 21, 25, 26, 782490)'}),
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
        'gallery.category': {
            'Meta': {'unique_together': "[('slug', 'artist'), ('title', 'artist')]", 'object_name': 'Category'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['artist.Artist']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preferred_child': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gallery_category_preferred_child'", 'null': 'True', 'to': "orm['gallery.Series']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gallery.extendedmedia': {
            'Meta': {'unique_together': "(('slug', 'artist'),)", 'object_name': 'ExtendedMedia'},
            'api_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['artist.Artist']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'media_type': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '20'}),
            'piece': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Piece']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gallery.piece': {
            'Meta': {'unique_together': "(('slug', 'artist'),)", 'object_name': 'Piece'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['artist.Artist']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dimensions': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'for_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'preferred_child': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gallery_piece_preferred_child'", 'null': 'True', 'to': "orm['gallery.ExtendedMedia']"}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Series']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gallery.series': {
            'Meta': {'unique_together': "(('slug', 'artist'),)", 'object_name': 'Series'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['artist.Artist']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Category']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preferred_child': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gallery_series_preferred_child'", 'null': 'True', 'to': "orm['gallery.Piece']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'typekit': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['gallery']
