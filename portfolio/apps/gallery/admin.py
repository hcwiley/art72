from apps.gallery.models import Category, ExtendedMedia, Piece, Series
from django.contrib import admin
from apps.gallery.forms import CategoryAdminForm, SeriesAdminForm, PieceAdminForm
         
def save_entity(modeladmin, request, queryset):         
    for obj in queryset:
        obj.save()
save_entity.short_description = "Save selected models."

def get_default_video_thumb(modeladmin, request, queryset):
    print queryset
    for obj in queryset:
        for media in obj.children():
            media.set_thumb()
get_default_video_thumb.short_description = "Update video thumbnail to be current video thumbnail default from video provider" 

class ExtendedMediaInline(admin.TabularInline):
    model = ExtendedMedia
    extra = 1

class PieceAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'date', 'title',)
    inlines = [ExtendedMediaInline]
    list_display = ['title', 'series', 'artist']
    ordering = ['title']
    form = PieceAdminForm
    actions = [save_entity, get_default_video_thumb]
    fieldsets = (
        (None, {
            'fields': ('artist', 'title', 'series', 'description', 'date', 'materials', 'dimensions', 'preferred_child'),
        }),
        ('For Sale Options (default is Not For Sale)', {
            'classes': ('collapse',),
            'fields': (('for_sale', 'price'),)
        }),
    )
    
class PieceInline(admin.TabularInline):
    model = Piece
    extra =1
    
class SeriesAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'date', 'materials']
    inlines = [PieceInline]
    list_display = ['title', 'category', 'artist']
    ordering = ['title']
    form = SeriesAdminForm
    actions = [save_entity]
    
class SeriesInline(admin.TabularInline):    
    model = Series
    extra = 1
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    inlines = [SeriesInline]
    list_display = ['title', 'artist']
    ordering = ['title']
    form = CategoryAdminForm
    actions = [save_entity]    

admin.site.register(Piece, PieceAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ExtendedMedia)