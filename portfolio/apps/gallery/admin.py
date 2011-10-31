from gallery.models import *
from django.contrib import admin

class ExtendedImageInline(admin.TabularInline):
    model = ExtendedImage
    extra = 1
    readonly_fields = ('orig_file_name',)


class PieceAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'extendedimage__orig_file_name',)
    inlines = [ExtendedImageInline]
    
    
admin.site.register(Piece, PieceAdmin)