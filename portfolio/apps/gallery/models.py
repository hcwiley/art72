from django.conf import settings
from django.contrib import admin
from django.db.models.signals import post_delete
from django.db import models
from django.dispatch import receiver 
import sorl
from uuid import uuid4
import Image
import os
from artist.models import Artist

class Category(models.Model):
    """
    A category class, could be anything really.
    e.g. Publications, Posters, Website, etc.
    """
    name = models.CharField(max_length=100)
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
    title = models.CharField(max_length=400)
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
    
class ExtendedImage(models.Model):
    """
    An Extended Image class. This is a single image.
    Guarantees a unique and valid file name.
    Detects file format and appends the appropriate extension.
    Saves image file into a dated directory to reduce the chance of degraded 
        performance from too many files in a directory.
        #TODO: maybe adopt the cache's folder structure instead of using dates
    """
    image = sorl.thumbnail.ImageField(upload_to='images/%Y/%m/%d')
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
        sorl.thumbnail.delete(self.image) 
        super(ExtendedImage, self).delete(*args, **kwargs)


@receiver(post_delete, sender=ExtendedImage, weak=False)
def delete_image_on_file(sender, instance, **kwargs):
    """
    Delete the image and thumb files of the ExtendedImage sender post delete.
    While this will delete the files, it may leave empty directories.
    """
    sorl.thumbnail.delete(instance.image)
    