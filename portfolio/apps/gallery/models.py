from django.conf import settings
from django.contrib import admin
from django.db.models.signals import post_delete
from django.db import models
from django.dispatch import receiver
from uuid import uuid4
import Image

#class Category(models.Model):
#    """
#    A category class, could be anything really.
#    e.g. Publications, Posters, Website, etc.
#    """
#    name = models.CharField(max_length=100, unique=True)
#    artist = models.ForeignKey(Artist)
#    
#    def __unicode__(self):
#        return self.name
#    
#    class Meta:
#        verbose_name_plural = "Categories"
#        
#admin.site.register(Category)
#
#class Series(models.Model):
#    """
#    A Series class.
#    """
#    name = models.CharField(max_length=400, unique=True)
#    category = models.ForeignKey(Category)
#    
#    def __unicode__(self):
#        return self.name
#    
#    class Meta:
#        verbose_name_plural = "Series"
#
#admin.site.register(Series)
#
class Piece(models.Model):
    """
    A Piece class. This represents the abstract idea of a piece of work.
    A piece can be represented by many extended images.
    """
    title = models.CharField(max_length=400, unique=True)
    description = models.TextField(null=True, blank=True)

    def default_img(self):
        return self.extendedimage_set.all()[0]

    def get_url(self):
        return self.pk

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
    