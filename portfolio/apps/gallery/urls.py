from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^(?P<artist>[^/]+)/(?P<category>[^/]+)/(?P<series>[^/]+)/(?P<piece>[^/]+)$', 'gallery.views.piece'),
    (r'^(?P<artist>[^/]+)/(?P<category>[^/]+)/(?P<series>[^/]+)$', 'gallery.views.series'),
    (r'^(?P<artist>[^/]+)/(?P<category>[^/]+)$', 'gallery.views.category'),
    (r'^(?P<artist>[^/]+)$', 'gallery.views.artist'),
)