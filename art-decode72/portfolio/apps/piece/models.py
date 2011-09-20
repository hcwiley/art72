from django.db import models
from django import forms
from django.conf import settings
#from django.core.files import ContentFile
from django.contrib.admin import widgets 
from django.contrib import admin
from django.template.defaultfilters import slugify
from artist.models import *

import Image

class MyImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    thumb = models.ImageField(upload_to='gallery/thumbs', blank=True, null=True, editable=False)
    thumbsize = (300,300)
    
    class Meta:
        ordering = ['image']
        
    def __unicode__(self):
        return self.image.url
    
    def saveThumb(self):
        path = '%s/%s' % (settings.MEDIA_ROOT, self.image)
        img = Image.open(path)
        img = img.resize(self.thumbsize, Image.ANTIALIAS)
        path = path.replace('gallery', 'gallery/thumbs')
        img.save(path)
        self.thumb = path
    
    def save(self, *args, **kwargs):
        super(MyImage, self).save(*args, **kwargs)
        self.saveThumb()
    
class Series(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    slug=models.SlugField(max_length=160,blank=True,editable=False)
    artist = models.ForeignKey(Artist,blank=True,editable=False)
    
    def update(self):
        if(self.artist == None):
            self.artist = Users.objects.filter(pk='2')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.artist = Artist.objects.all()[0] if len(Artist.objects.all()) > 0 else Artist.objects.get_or_create(user=User.objects.all()[0])
        super(Series, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.slug

class SeriesForm(forms.Form):
    name = forms.CharField(max_length=400)
    description = forms.CharField(widget=forms.Textarea(), required=False)

class Piece(models.Model):
    title = models.CharField(max_length=400)
    default_image = models.ForeignKey(MyImage, related_name='%(app_label)s_%(class)s_default_image', null=True, blank=True) 
    date = models.DateField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    series = models.ManyToManyField(Series, related_name='%(app_label)s_%(class)s_series', null=True, blank=True)
    slug=models.SlugField(max_length=160,blank=True,editable=False)
    description = models.TextField(null=True, blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=True)
    
    def update(self):
        if(self.artist == None):
            self.artist = Users.objects.filter(pk='2')
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.artist == None and len(Artist.objects.all()) > 0:
            self.artist = Artist.objects.all()[0]
        self.slug = slugify(self.title)
        super(Piece, self).save(*args, **kwargs)

    def listSeries():
        sers = Series.objects.all()
        series = []
        for s in sers:
            series.append(s.name)
        return sers
    
class PieceForm(forms.Form):
    title = forms.CharField(max_length=400)
    default_image = forms.ImageField(widget=forms.FileInput(), required=False) 
    date = forms.DateField(widget=widgets.AdminDateWidget(), required=False)
    price = forms.IntegerField(required=False)
    series = forms.CharField(max_length=400)