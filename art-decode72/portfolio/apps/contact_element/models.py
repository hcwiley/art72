from django.db import models
from django import forms
from django.forms import ModelForm
#from django.core.files import ContentFile
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
    
LINK_TYPES = (('http://', 'webpage'), ('callto://', 'phone'), ('mailto://', 'email'), ('', 'file'))

class ContactElement(models.Model):
    displayed = models.CharField(max_length=400)
    links_to = models.CharField(max_length=500)
    file = models.FileField(upload_to='uploaded', null=True, blank=True)
    type = models.CharField(max_length = 30, choices=LINK_TYPES)
    
    def __unicode__(self):
        return self.displayed
    def html(self):
        return "<a href='%s%s' title='%s'>%s</a>" % (self.type, self.links_to, self.links_to, self.displayed)

class ContactElementForm(forms.Form):
    display = forms.CharField(max_length=400)
    links_to = forms.CharField(max_length=400)
    file = forms.FileField()
    type = forms.ChoiceField(choices=LINK_TYPES)
    
class VideoUser(models.Model):
    username = models.CharField(max_length=400)
    url = models.URLField(unique=False)
    type = models.CharField(max_length=400)
    slug = models.SlugField(max_length=160,blank=True,editable=False)
    
    class Meta:
        ordering = ['url']

    def with_http(self):
        if self.url.startswith('http://'):
            return self.url
        else:
            return 'http://' + self.url

    def __unicode__(self):
        return '%s: %s' % (self.username, self.type)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(VideoUser, self).save(*args, **kwargs)
        
class VideoUserForm(ModelForm):
    class Meta:
        model = VideoUser
        
class VideoLink(models.Model):
    title = models.CharField(max_length=400)
    url = models.URLField(unique=False)
    account = models.ForeignKey(VideoUser, verbose_name='video user its linked to', null=True, blank=True)
    slug=models.SlugField(max_length=160,blank=True, null=True, editable=False)
    
    class Meta:
        ordering = ['url']

    def with_http(self):
        if self.url.startswith('http://'):
            return self.url
        else:
            return 'http://' + self.url

    def __unicode__(self):
        if self.url.startswith('http://'):
            return self.url[7:]
        else:
            return self.url
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(VideoLink, self).save(*args, **kwargs)
        
class VideoLinkForm(ModelForm):
    class Meta:
        model = VideoLink
