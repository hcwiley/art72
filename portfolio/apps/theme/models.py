from django.contrib import admin
from django.db import models
from artist.models import Artist

class CssFileWrapper(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='css')
    blurb = models.TextField()
    #tags = ??
    
    def __unicode__(self):
        return self.name

admin.site.register(CssFileWrapper)

class Theme(models.Model):
    """
    All the things about the (css, levels of deepness, names).
    TODO: better names for the css field
    """
    name = models.CharField(max_length=50)
    site_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_site_css')
    index_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_index_css')
    contact_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_contact_css')
    top_level_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_top_level_css') 
    category_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_category_css')
    series_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_series_css')
    piece_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_piece_css')
    color_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_color_css')
    font_css = models.ForeignKey(CssFileWrapper, related_name='%(app_label)s_%(class)s_font_css')
    #deepness 
    artist = models.ForeignKey(Artist)
    def __unicode__(self):
        return self.name
    
    def to_html(self):
        html = ''
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.site_css.file.url
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.top_level_css.file.url
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.category_css.file.url
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.series_css.file.url
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.piece_css.file.url
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.font_css.file.url
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.color_css.file.url
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.index_css.file.url
        html += "<link type='text/css' rel='stylesheet' href='%s'/>" % self.contact_css.file.url
        return html

admin.site.register(Theme)
