from django.conf import settings
from django.contrib import admin
from django.db.models.signals import post_delete
from django.db import models
from django.dispatch import receiver 
from sorl import thumbnail
from uuid import uuid4
import Image
import os
from artist.models import Artist
from django.template.defaultfilters import slugify

class Category(models.Model):
    """
    A category class, could be anything really.
    e.g. Publications, Posters, Website, etc.
    """
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist)
    slug = models.SlugField()
    #TODO: probably going to need some sort of rich/mark up text editing for descriptions, some way to put links?
    #TODO: at least make some decent admin forms (auto slug populate, use the image admin, etc.
    #TODO: start making forms and hook up both dajax (the data one and the presentation one), at least for testing
    #TODO: should slugs update automagically? when the name changes? should we ask the user? what if we do something like stack overflow e.g. use a unique number, and then add in the (not required unique or correct) slug 
    def get_absolute_url(self): 
        return os.path.join(self.artist.get_absolute_url(), self.slug)
    
    def series(self):
        return self.series_set.all()
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        #TODO: this will bomb fo sho if it's not unique. we got to decide on some url schema and then enforce it. until then i'll stick with this.
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        unique_together = ("name", "artist")
        verbose_name_plural = "Categories"
        
admin.site.register(Category)


class Series(models.Model):
    """
    A Series class.
    """
    artist = models.ForeignKey(Artist)
    name = models.CharField(max_length=400)
    category = models.ForeignKey(Category, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    
    def default_piece(self):
        #TODO: add in some error handling, here and elsewhere
        try:
            return self.piece_set.all()[0]
        except:
            return None 
    
    def get_absolute_url(self):    
        if self.category:
            return os.path.join(self.category.get_absolute_url(), self.slug)
        else:
            return os.path.join(self.artist.get_absolute_url(), self.slug)
    
    def pieces(self):
        return self.piece_set.all()
        
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        #TODO: this will bomb fo sho if it's not unique. we got to decide on some url schema and then enforce it. until then i'll stick with this.
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Series, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = "Series"

admin.site.register(Series)


class Piece(models.Model):
    """
    A Piece class. This represents the abstract idea of a piece of work.
    A piece can be represented by many extended images.
    """
    title = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    series = models.ForeignKey(Series, null=True, blank=True)
    artist = models.ForeignKey(Artist)
    slug = models.SlugField()

    def all_imgs(self):
        return self.extendedimage_set.all()

    def default_img(self):
        return self.extendedimage_set.all()[0]

    def get_absolute_url(self):
        if self.series:
            return os.path.join(self.series.get_absolute_url(), self.slug)
        else:
            return os.path.join(self.artist.get_absolute_url(), self.slug)

    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        #TODO: this will bomb fo sho if it's not unique. we got to decide on some url schema and then enforce it. until then i'll stick with this.
        if self.slug == '':
            self.slug = slugify(self.title)
        super(Piece, self).save(*args, **kwargs)


try:
    MAX_IMAGE_SIZE = settings.MAX_IMAGE_SIZE 
except AttributeError:
    MAX_IMAGE_SIZE = (1200, 1200)
    
class ExtendedImage(models.Model):
    """
    An Extended Image class. This is a single image.
    Guarantees a unique and valid file name.
    Detects file format and appends the appropriate extension.
    Saves image file into a dated directory to reduce the chance of degraded 
        performance from too many files in a directory.
        #TODO: maybe adopt the cache's folder structure instead of using dates
    """
    image = thumbnail.ImageField(upload_to='images/%Y/%m/%d')
    orig_file_name = models.CharField(max_length=100, editable=False, verbose_name="original file name")
    piece = models.ForeignKey(Piece)
    artist = models.ForeignKey(Artist)
    
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
        #TODO: check file size rather than max resolution
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
        
    def delete(self, *args, **kwargs):
        """
        Delete the actual image and all associated thumbnails and then delete.
        """
        thumbnail.delete(self.image) 
        super(ExtendedImage, self).delete(*args, **kwargs)


@receiver(post_delete, sender=ExtendedImage, weak=False)
def delete_image_on_file(sender, instance, **kwargs):
    """
    Delete the image and thumb files of the ExtendedImage sender post delete.
    While this will delete the files, it may leave empty directories.
    """
    thumbnail.delete(instance.image)
    