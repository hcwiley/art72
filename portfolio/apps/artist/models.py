from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import admin
from django.dispatch import receiver 
from django.db.models.signals import post_save, pre_save
from django.utils.encoding import smart_str
import os
from django.contrib.sites.models import Site
from django.contrib.localflavor.us.forms import USPhoneNumberField
from apps.theme.models import Theme
from django.contrib.localflavor.us.models import PhoneNumberField

class Artist(models.Model):
    """
    Extra user info that makes up an Artist.
    """
    # user data
    user = models.OneToOneField(User, null=True, blank=True)
    statement = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/%Y/%m/%d', blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    # theme stuff
    theme = models.OneToOneField(Theme, blank=True, null=True) #TODO: once default system data is in place, make this mandatory
    # video links
    vimeo_id = models.CharField(max_length=50, blank=True, null=True)
    youtube_id = models.CharField(max_length=50, blank=True, null=True)
    #TODO: theme should be required, will just need to have a default to fall back on
    
    def get_absolute_url(self): 
        current_site = Site.objects.get_current()
        return "http://%s.%s" % (self.user.username, current_site.domain)
    
    def get_gallery_url(self): 
        return os.path.join(self.get_absolute_url(), "gallery")
        
    def __unicode__(self):
        if self.user.get_full_name() != '':
            return self.user.get_full_name()
        else:
            return self.user.username 
    
    def save(self, *args, **kwargs):
#        if self.theme == None:
#            self.theme = Theme.objects.create()
        super(Artist, self).save(*args, **kwargs) 
        
@receiver(post_save, sender=User, weak=False)
def delete_image_on_file(sender, instance, raw, created, using, **kwargs):
    if created:
        Artist.objects.create(user=instance)
        
@receiver(pre_save, sender=User, weak=False)
def ensure_unique_email(sender, instance, raw, using, **kwargs):
    users = User.objects.filter(email__iexact=instance.email)
    if users and users[0].id != instance.id:
        raise ValidationError("The email '%s' is already associated with another account." % instance.email)
    users = User.objects.filter(username__iexact=instance.username)
    if users and users[0].id != instance.id:
        raise ValidationError("The username '%s' is already associated with another account." % instance.username)
