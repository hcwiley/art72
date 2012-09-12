from django.contrib import admin
from apps.theme.models import TypeKitFont, FontPair, ColorPalette, Layout, Theme
from apps.theme.forms import ThemeAdminForm

class FontAdmin(admin.ModelAdmin):
    prepopulated_fields = {"typekit": ("title",)}

class ColorPaletteAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('c1', 'c2', 'c3', 'c4', 'c5'),
            'description': "c1-c5 - any valid CSS color in the form #fff, #abcdef, f2b, 23fa2e, etc. '#' will be automagically added if not supplied."
        }),
    )
    
class FontPairAdmin(admin.ModelAdmin):
    pass    
    
class LayoutAdmin(admin.ModelAdmin):
    pass

class ThemeAdmin(admin.ModelAdmin):
    form = ThemeAdminForm
    
admin.site.register(TypeKitFont, FontAdmin)
admin.site.register(ColorPalette, ColorPaletteAdmin)
admin.site.register(FontPair, FontPairAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Layout, LayoutAdmin)