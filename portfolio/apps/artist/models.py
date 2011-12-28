from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import admin
from django.dispatch import receiver 
from django.db.models.signals import post_save, pre_save
from django.utils.encoding import smart_str
import urllib
from django.contrib.sites.models import Site

class Artist(models.Model):
    """
    Extra user info that makes up an Artist.
    """
    #TODO: when checking for unique email, check for things like 'zackdever@gmail.com' vs 'zackdever+foo@gmail.com' and periods. not sure if this is specific to gmail or not
    #TODO: maybe store some other value of 'displayed name?' this may be on the theme...
    user = models.OneToOneField(User)
    statement = models.TextField(null=True, blank=True)
    #theme = models.ForeignKey(Theme)
    
    def get_absolute_url(self): 
        current_site = Site.objects.get_current()
        return "http://%s.%s" % (self.user.username, current_site.domain)
        
    def __unicode__(self):
        if self.user.get_full_name() != '':
            return self.user.get_full_name()
        else:
            return self.user.username 
    
    def get_theme(self):
        try:
            return self.theme_set.all()[0]
        except:
            return None

admin.site.register(Artist)

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