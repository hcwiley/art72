from django.db import models
from django import forms
#from django.core.files import ContentFile
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from contact_element.models import *
    
class Artist(models.Model):
    user = models.ForeignKey(User, unique=True)
    nickname = models.CharField(max_length=400)
    site_name = models.CharField(max_length=400)
    contact_elements = models.ManyToManyField(ContactElement, related_name='%(app_label)s_%(class)s_contact_elements', null=True, blank=True)
    #css = models.File ?
    #template = models.Choice?
    
    def __unicode__(self):
        return slugify(self.user)
    
    def getContactElements(self):
        return self.contact_elements.objects.all()
    
    def save(self, *args, **kwargs):
        if(self.nickname == None):
            self.nickname = '%s %s' % (self.user.first_name, self.user.last_name)
        if(self.site_name == None):
            self.site_name = '%s %s' % (self.user.first_name, self.user.last_name)
        super(Artist, self).save(*args, **kwargs)
    
    def update(self):
        if(self.nickname == None):
            self.nickname = '%s %s' % (self.user.first_name, self.user.last_name)
        if(self.site_name == None):
            self.site_name = '%s %s' % (self.user.first_name, self.user.last_name)
