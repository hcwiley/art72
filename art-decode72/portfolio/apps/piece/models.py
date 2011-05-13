from django.db import models
#from django.core.files import ContentFile 
from django.contrib import admin
from django.template.defaultfilters import slugify

class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    
    class Meta:
        ordering = ['image']
        
    def __unicode__(self):
        return self.image.url
    
class Series(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    slug=models.SlugField(max_length=160,blank=True,editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Series, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.slug
    
class Piece(models.Model):
    title = models.CharField(max_length=400)
    default_image = models.ForeignKey(Image, related_name='%(app_label)s_%(class)s_default_image', null=True, blank=True) 
    date = models.DateField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    series = models.ManyToManyField(Series, related_name='%(app_label)s_%(class)s_series', null=True, blank=True)
    slug=models.SlugField(max_length=160,blank=True,editable=False)
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Piece, self).save(*args, **kwargs)

    def listSeries():
        sers = Series.objects.all()
        series = []
        for s in sers:
            series.append(s.name)
        return sers
    
