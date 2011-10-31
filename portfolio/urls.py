from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

urlpatterns = ()

if settings.DEBUG:
    # let django serve static media
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.MEDIA_URL, 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        )