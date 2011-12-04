from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<category>.+)/(?P<series>.+)/(?P<piece>.+)$', 'gallery.views.piece'),
    (r'^(?P<category>.+)/(?P<series>.+)$', 'gallery.views.series'),
    (r'^(?P<category>.+)$', 'gallery.views.category'),
    (r'^$', 'gallery.views.home'),
)