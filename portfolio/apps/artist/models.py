from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    """
    Extra user info that makes up an Artist.
    TODO:
        everything
    """
    user = models.ForeignKey(User, unique=True)