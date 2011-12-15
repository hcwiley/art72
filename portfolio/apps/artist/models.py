from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.dispatch import receiver 
from django.db.models.signals import post_save

class Artist(models.Model):
    """
    Extra user info that makes up an Artist.
    TODO:
        everything
    """
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 100, null=True, blank=True)
    statement = models.TextField(null=True, blank=True)
    #theme = models.ForeignKey(Theme)
    
    def __unicode__(self):
        if self.name:
            return self.name
        return self.user.username 
    
    def get_theme(self):
        try:
            return self.theme_set.all()[0]
        except:
            return None

admin.site.register(Artist)

@receiver(post_save, sender=User, weak=False)
def delete_image_on_file(sender, instance, created, using, **kwargs):
    if created:
        Artist.objects.create(user=instance)