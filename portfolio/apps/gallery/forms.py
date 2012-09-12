from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.models import User
from apps.gallery.models import *

class CategoryAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)
        self.fields['preferred_child'].queryset = self.instance.gallery_children()
    class Meta:
        model = Category

class SeriesAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SeriesAdminForm, self).__init__(*args, **kwargs)
        self.fields['preferred_child'].queryset = self.instance.gallery_children()
        self.fields['category'].queryset = self.instance.artist.category_set
    class Meta:
        model = Series

class PieceAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PieceAdminForm, self).__init__(*args, **kwargs)
        self.fields['preferred_child'].queryset = self.instance.gallery_children()
        self.fields['series'].queryset = self.instance.artist.series_set
    class Meta:
        model = Piece

