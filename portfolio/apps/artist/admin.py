from django.contrib import admin
from django.contrib.auth.models import User
from apps.artist.models import Artist
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class ArtistInline(admin.StackedInline):
    model = Artist

class UserAdmin(UserAdmin):
    inlines = [ ArtistInline, ]

admin.site.register(User, UserAdmin)