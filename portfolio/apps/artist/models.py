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
    #css = ??

admin.site.register(Artist)