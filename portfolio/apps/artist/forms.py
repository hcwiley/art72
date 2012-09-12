from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.models import User
from apps.artist.models import Artist

class AccountForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ('display_name', 'location', 'statement', 'bio', 'resume', 'phone', 'vimeo_id', 'youtube_id')