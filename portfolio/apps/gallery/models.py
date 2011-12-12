from django.conf import settings
from django.contrib import admin
from django.db.models.signals import post_delete
from django.db import models
from django.dispatch import receiver
from uuid import uuid4
import Image
import os

class Artist(models.Model):
    """
    Extra user info that makes up an Artist.
    TODO:
        everything
    """
    #user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length = 100)
    #theme = models.ForeignKey(Theme)
    #user_theme = models.For
    
    def __unicode__(self):
        return self.name
    
    def get_theme(self):
        try:
            return self.theme_set.all()[0]
        except:
            return None

admin.site.register(Artist)

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
    TODO:
        -better names for the css field
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


class Category(models.Model):
    """
    A category class, could be anything really.
    e.g. Publications, Posters, Website, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    artist = models.ForeignKey(Artist)
    
    def get_url(self):
        try:
            return str(self.pk)
        except:
            return '1'
    
    def series(self):
        return self.series_set.all()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        
admin.site.register(Category)

class Series(models.Model):
    """
    A Series class.
    """
    name = models.CharField(max_length=400, unique=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    artist = models.ForeignKey(Artist)
    
    def default_piece(self):
        #TODO: add in some error handling, here and elsewhere
        try:
            return self.piece_set.all()[0]
        except:
            return None 
    
    def get_url(self):
        try:
            if self.category:
                return os.path.join(self.category.get_url(), str(self.pk))
            else:
                return str(self.pk)
        except:
            return '1' 
    
    def pieces(self):
        return self.piece_set.all()
        
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Series"

admin.site.register(Series)

class Piece(models.Model):
    """
    A Piece class. This represents the abstract idea of a piece of work.
    A piece can be represented by many extended images.
    """
    #TODO: why is this title and everything else is name?
    title = models.CharField(max_length=400, unique=True)
    description = models.TextField(null=True, blank=True)
    series = models.ForeignKey(Series, null=True, blank=True)
    artist = models.ForeignKey(Artist)

    def all_imgs(self):
        return self.extendedimage_set.all()

    def default_img(self):
        return self.extendedimage_set.all()[0]

    def get_url(self):
        try:
            if self.series:
                return os.path.join(self.series.get_url(), str(self.pk))
            else:
                return str(self.pk)
        except:
            return '1'

    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Piece, self).save(*args, **kwargs)

try:
    MAX_IMAGE_SIZE = settings.MAX_IMAGE_SIZE 
except AttributeError:
    MAX_IMAGE_SIZE = (1200, 1200)

try:
    THUMB_SIZE = settings.THUMB_SIZE
except AttributeError:
    THUMB_SIZE = (160, 160)
    
class ExtendedImage(models.Model):
    """
    An Extended Image class. This is a single image.
    Guarantees a unique and valid file name.
    Detects file format and appends the appropriate extension.
    Saves image file into a dated directory to reduce the chance of degraded 
        performance from too many files in a directory.
    TODO:
        thumbnails - https://code.djangoproject.com/wiki/ThumbNails
    """
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    orig_file_name = models.CharField(max_length=100, editable=False, verbose_name="original file name")
    piece = models.ForeignKey(Piece)
    artist = models.ForeignKey(Artist)
    
    def width(self):
        return self.image.width
    
    def height(self):
        return self.image.height
    
    def __unicode__(self):
        return self.image.url

    def get_url(self):
        return self.image.url

    def set_orig_file_name(self):
        """
        Save the original file name.
        If it greater than 100 char, take the first and last 50 chars.
        """
        if (len(self.image.name) > 100):
            self.orig_file_name = self.image.name[:50] + self.image.name[-50:]
        else:
            self.orig_file_name = self.image.name
        
    def rename_image_file(self):
        """
        Generate a UUID for the file name and 
        append the appropriate extension based off the format of the file.
        """
        img = Image.open(self.image)
        self.image.name = "%s.%s" % (uuid4(), img.format.lower())
        
    def do_resizes(self):
        """
        Only allow images to be MAX_IMAGE_SIZE.
        Create thumbnail of THUMB_SIZE after the resize.
        """
        img = Image.open(self.image.path)
        img.thumbnail(MAX_IMAGE_SIZE, Image.ANTIALIAS)
        img.save(self.image.path)
    
    def save(self, *args, **kwargs):
        """
        Clean up file names, images sizes, and then finally save.
        """
        self.set_orig_file_name()
        self.rename_image_file()
        super(ExtendedImage, self).save(*args, **kwargs)
        self.do_resizes()


@receiver(post_delete, sender=ExtendedImage, weak=False)
def delete_image_on_file(sender, instance, **kwargs):
    """
    Delete the image and thumb files of the ExtendedImage sender post delete.
    While this will delete the files, it may leave empty directories.
    """
    instance.image.delete(save=False)
    