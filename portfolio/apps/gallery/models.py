from django.conf import settings
from django.contrib import admin
from django.db.models.signals import post_delete
from django.db import models
from django.dispatch import receiver 
from sorl import thumbnail
from uuid import uuid4
from apps.artist.models import Artist
from itertools import chain
import Image
import os
from apps.gallery.utils import get_unique_slug
from django.template.context import Context
from django.template.loader import get_template 
from django.core.exceptions import ValidationError
from django.db.models import Count
import xml.dom.minidom
import urllib2
from urlparse import urlparse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

#TODO: use custom slug from djutils rather than the one i wrote. it does some nice things like truncate on whole word and most notably is not maintained by me.
class GalleryBase(models.Model):
    """
    The base class for the main gallery models - category, series, and piece.
    """
    artist = models.ForeignKey(Artist, default=None, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    description = models.TextField(blank=True, null=True)
    # must also have field 'preferred_child' 
    
    class Meta:
        abstract = True
        unique_together = ("slug", "artist")
    
    def children(self):
        """
        Must be implemented when subclassed.
        This is used in preferred_child.
        """
        return None
        
    def dashboard_url(self):
        return '/dashboard/work'
        
    def default_media(self):
        """
        The default media of the default child.
        """
        if self.preferred_child:
            return self.preferred_child.default_media()
        return None
    
    def is_empty(self):
        """
        True if there are no children - should not be displayed in gallery, only dashboard.
        OPTIMIZE: Cache/keep track of this rather than performing query, but we'll optimize when we have an optimization problem.
        """
        return not self.children().exists()    

class GalleryCategoryManager(models.Manager):
    def get_query_set(self):
        return super(GalleryCategoryManager, self).get_query_set().annotate(child_count=Count('series')).filter(child_count__gt=0)


class Category(GalleryBase):
    """
    A category class, could be anything really.
    e.g. Publications, Posters, Website, etc.
    """
    preferred_child = models.ForeignKey('Series', related_name='%(app_label)s_%(class)s_preferred_child', null=True, blank=True)
    objects = models.Manager()
    gallery_objects = GalleryCategoryManager()
        
    def gallery_children(self):
        return Series.gallery_objects.filter(category=self.pk)        
        
    def children(self):
        return self.series_set.all() 
    
    def dashboard_url(self):
        return '/dashboard/work/%s' % self.slug
    
    def get_absolute_url(self, relative=False): 
        return os.path.join(self.artist.get_gallery_url(), self.slug)

    def __unicode__(self):
        return self.title
        
    def clean(self):
        if self.preferred_child and self.preferred_child.category.pk != self.pk:
            raise ValidationError('The preferred series of a category must belong to that category.')
        
    def save(self, *args, **kwargs):
        if self.slug == '':
            max_length = Category._meta.get_field('slug').max_length
            self.slug = get_unique_slug(self.artist.category_set, self.title, max_length)
        if not self.preferred_child and self.children():
            self.preferred_child = self.children()[0]
        super(Category, self).save(*args, **kwargs)        

    class Meta:
        unique_together = [("slug", "artist"), ("title", "artist")]
        verbose_name_plural = "Categories"
        
class GallerySeriesManager(models.Manager):
    def get_query_set(self):
        return super(GallerySeriesManager, self).get_query_set().annotate(child_count=Count('piece')).filter(child_count__gt=0)

class Series(GalleryBase):
    """
    A Series class.
    """
    category = models.ForeignKey(Category, blank=True, null=True)
    date = models.IntegerField(null=True, blank=True)
    preferred_child = models.ForeignKey('Piece', related_name='%(app_label)s_%(class)s_preferred_child', null=True, blank=True)
    objects = models.Manager()
    gallery_objects = GallerySeriesManager()

    def gallery_children(self):
        return Piece.gallery_objects.filter(series=self.pk) 
    
    def children(self):
        return self.piece_set.all()    

    def dashboard_url(self):
        #TODO: make this and absolute_url less redundant...
        if self.category:
            return os.path.join(self.category.dashboard_url(), self.slug)
        else:
            return '/dashboard/work/%s' % self.slug
    
    
    def get_absolute_url(self):    
        if self.category:
            return os.path.join(self.category.get_absolute_url(), self.slug)
        else:
            return os.path.join(self.artist.get_absolute_url(), self.slug)
                
    def __unicode__(self):
        return self.title
    
    def clean(self):
        if self.category and self.category.artist.pk != self.artist.pk:
            raise ValidationError("The series' category must be associated with the same artist.")
        if self.preferred_child and self.preferred_child.series.pk != self.pk:
            raise ValidationError('The preferred piece of a series must belong to that series.')
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            max_length = Series._meta.get_field('slug').max_length
            self.slug = get_unique_slug(self.artist.series_set, self.title, max_length)
        if self.preferred_child == None and self.children():
            self.preferred_child = self.children()[0]
            print 'should hav ea preferred child'
        super(Series, self).save(*args, **kwargs)  
        
    class Meta:
        unique_together = ("slug", "artist")
        verbose_name_plural = "Series"

class GalleryPieceManager(models.Manager):
    def get_query_set(self):
        return super(GalleryPieceManager, self).get_query_set().annotate(c=Count('extendedmedia')).filter(c__gt=0)

class Piece(GalleryBase):
    """
    A Piece class. This represents the abstract idea of a piece of work.
    A piece can be represented by many extended images.
    """
    materials = models.CharField(max_length=50, null=True, blank=True)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    series = models.ForeignKey(Series, null=True, blank=True)
    for_sale = models.BooleanField()
    price = models.IntegerField(null=True, blank=True, help_text="Only shown if marked for sale.")
    date = models.IntegerField(null=True, blank=True)
    preferred_child = models.ForeignKey('ExtendedMedia', related_name='%(app_label)s_%(class)s_preferred_child', null=True, blank=True)
    objects = models.Manager()
    gallery_objects = GalleryPieceManager()

    def gallery_children(self):
        return ExtendedMedia.gallery_objects.filter(piece=self.pk) 
    
    def children(self):
        return self.extendedmedia_set.all()

    def get_absolute_url(self):
        if self.series:
            return os.path.join(self.series.get_absolute_url(), self.slug)
        else:
            return os.path.join(self.artist.get_absolute_url(), self.slug)
        
    def dashboard_url(self):
        #TODO: make this and absolute_url less redundant...
        if self.series:
            return os.path.join(self.series.dashboard_url(), self.slug)
        else:
            return '/dashboard/work/%s' % self.slug        
        
    def pretty_for_sale(self):
        return 'for sale' if self.for_sale else 'not for sale'
    
    def form_as_edit(self):
        html = '<h3>title</h3>'
        html += "<h4 class='piece-info' id='title'>%s</h4>" % self.title
        html += "<h5 class='edit-button'>edit</h5>"
        html += "<br>"
        html += '<h3>description</h3>'
        html += "<h4 class='piece-info' id='description'>%s</h4>" % self.description
        html += "<h5 class='edit-button'>edit</h5>"
        html += "<br>"
        html += '<h3>date</h3>'
        html += "<h4 class='piece-info' id='date'>%s</h4>" % self.date
        html += "<h5 class='edit-button'>edit</h5>"
        html += "<br>"
        html += '<h3>price</h3>'
        html += "<h4 class='piece-info' id='price'>%s</h4>" % self.price
        html += "<h5 class='edit-button'>edit</h5>"
        html += "<br>"
        return html
    
    def default_media(self, size=None , media=None):
        if media is None:
            media = self.preferred_child
        return media
    
    def __unicode__(self):
        return self.title

    def clean(self):
        if self.series and self.series.artist.pk != self.artist.pk:
            raise ValidationError("The piece's series must be associated with the same artist.")
        if self.preferred_child and self.preferred_child.piece.pk != self.pk:
            raise ValidationError('The preferred image/video of a piece must belong to that piece.')

    def save(self, *args, **kwargs):
        if self.slug == '':
            max_length = Piece._meta.get_field('slug').max_length
            self.slug = get_unique_slug(self.artist.piece_set, self.title, max_length)
        if not self.preferred_child and self.children():
            self.preferred_child = self.children()[0]
        super(Piece, self).save(*args, **kwargs)  

    class Meta:
        unique_together = ("slug", "artist")

try:
    MAX_IMAGE_SIZE = settings.MAX_IMAGE_SIZE 
except AttributeError:
    MAX_IMAGE_SIZE = (1400, 1400) 

class ExtendedMedia(GalleryBase):
    # REMEMBER TO CHANGE THIS IN DATA MIGRATION - VIMEO WAS 0, YOUTUBE WAS 1
    IMAGE = 0
    VIMEO = 1
    YOUTUBE = 2    
    MEDIA_TYPES = (
        (IMAGE, 'image'),
        (VIMEO, 'vimeo'),
        (YOUTUBE, 'youtube'),
    )
    piece = models.ForeignKey(Piece)
    image = thumbnail.ImageField(upload_to='images/%Y/%m/%d')
    media_type = models.SmallIntegerField(max_length=20, choices=MEDIA_TYPES)
    api_id = models.CharField(max_length=50, blank=True, null=True) 
    objects = models.Manager()
    gallery_objects = models.Manager()
    __original_image = None
    
    def __init__(self, *args, **kwargs):
        super(ExtendedMedia, self).__init__(*args, **kwargs)
        self.__original_image = self.image
    
    @property
    def preferred_child(self):
        return self
        
    def gallery_children(self):
        return self.children()
        
    def children(self):
        return ExtendedMedia.objects.filter(pk=self.pk)
        
    def is_video(self):
        return self.media_type == ExtendedMedia.VIMEO or self.media_type == ExtendedMedia.YOUTUBE

    def save(self, *args, **kwargs):
        if self.slug == '':
            max_length = ExtendedMedia._meta.get_field('slug').max_length
            self.slug = get_unique_slug(self.artist.extendedmedia_set, self.title, max_length)
        image_changed = self.image != self.__original_image
        if image_changed:
            self.rename_image_file()
            self.__original_image = self.image
        super(ExtendedMedia, self).save(*args, **kwargs)
        if image_changed:
            self.do_resizes()
    
    def __unicode__(self):
        return self.title
    
    def default_media(self):
        """
        Returns the underlying image file.
        Used to maintain base implementation of GalleryBase in Piece.
        """
        return self.image
    
    def get_video_url(self):
        if self.is_video():
            if self.media_type == ExtendedMedia.YOUTUBE:
                return "http://www.youtube.com/embed/%s" % self.api_id #TODO: on clean, do some validation to make sure video/image/api id/etc all match up
            elif self.media_type == ExtendedMedia.VIMEO:
                return "http://player.vimeo.com/video/%s" % self.api_id 
        return None    
    
    def get_url(self):
        """
        Gets the url of the underlying image file.
        """
        # Probably do some kind of check here at some point...
        #if self.media_type == self.IMAGE:
        return self.image.url
    
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
        """
        img = Image.open(self.image.path)
        img.thumbnail(MAX_IMAGE_SIZE, Image.ANTIALIAS)
        img.save(self.image.path)
    
    def set_thumb(self):
        if self.media_type == ExtendedMedia.VIMEO:
            url = 'http://vimeo.com/api/v2/video/%s.xml' % self.api_id
            file = NamedTemporaryFile(delete=True)
            file.write(urllib2.urlopen(url).read())
            file.flush()
            dom = xml.dom.minidom.parse(file.name)
            thumb = dom.getElementsByTagName('thumbnail_large')
            url = thumb[0].childNodes[0].data
            file.close()
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib2.urlopen(url).read())
            img_temp.flush()
            self.image.save(self.image.name , File(img_temp))
            img_temp.close()
            return True
        elif self.media_type == ExtendedMedia.YOUTUBE:
            url = 'http://img.youtube.com/vi/%s/0.jpg' % self.api_id
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib2.urlopen(url).read())
            img_temp.flush()
            self.image.save(self.image.name , File(img_temp))
            img_temp.close()
            return True
    
    def json_location(self):
        if self.media_type == ExtendedMedia.VIMEO:
            return 'http://vimeo.com/api/v2/%s/all_videos.json?callback=?' % self.artist.vimeo_id
        elif self.media_type == ExtendedMedia.YOUTUBE:
            return 'https://gdata.youtube.com/feeds/api/videos?author=%s&alt=json&prettyprint=true' % self.artist.youtube_id
        return None
    
    def clean(self):
        if self.piece.artist.pk != self.artist.pk:
            raise ValidationError("A media's piece must belong to its artist.")
        
    def delete(self, *args, **kwargs):
        """
        Delete the actual image and all associated thumbnails and then delete.
        """
        thumbnail.delete(self.image) 
        super(ExtendedMedia, self).delete(*args, **kwargs)    

@receiver(post_delete, sender=ExtendedMedia, weak=False)
def delete_image_on_file(sender, instance, **kwargs):
    """
    Delete the image and thumb files of the ExtendedMedia sender post delete.
    While this will delete the files, it may leave empty directories.
    """
    thumbnail.delete(instance.image)

    
