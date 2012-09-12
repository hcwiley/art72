from django.forms.models import ModelForm
from apps.theme.models import Theme, Layout

class ThemeAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ThemeAdminForm, self).__init__(*args, **kwargs)
        self.fields['site_layout'].queryset = Layout.site_objects
        self.fields['piece_layout'].queryset = Layout.piece_objects
        self.fields['series_layout'].queryset = Layout.series_objects
        self.fields['category_layout'].queryset = Layout.category_objects
    class Meta:
        model = Theme