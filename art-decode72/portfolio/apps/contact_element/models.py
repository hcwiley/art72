from django.db import models
from django import forms
#from django.core.files import ContentFile
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
    
LINK_TYPES = (('http://', 'webpage'), ('callto://', 'phone'), ('mailto://', 'email'), ('', 'file'))

class ContactElement(models.Model):
    displayed = models.CharField(max_length=400)
    links_to = models.CharField(max_length=500)
    file = models.FileField(upload_to='uploaded')
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
