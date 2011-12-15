from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Artist(models.Model):
    """
    Extra user info that makes up an Artist.
    TODO:
        everything
    """
    #user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length = 100)
    statement = models.TextField(null=True, blank=True)
    #theme = models.ForeignKey(Theme)
    
    def __unicode__(self):
        return self.name
    
    def get_theme(self):
        try:
            return self.theme_set.all()[0]
        except:
            return None

admin.site.register(Artist)