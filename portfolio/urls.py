from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import redirect_to, direct_to_template
from gallery import urls as gallery_urls
from django.conf.urls.defaults import patterns, include
admin.autodiscover()

# basic stuff
urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin$', 'views.admin_add_slash'),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
)


if settings.DEBUG:
    # let django serve user generated media while in development
    urlpatterns += patterns('',
#TODO don't let people name their top level series admin, site_media, etc.
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    (r'^$', redirect_to, {'url': '/gallery'}),
    (r'^gallery/', include(gallery_urls)),
    (r'^gallery', redirect_to, {'url': '/gallery/'}), #TODO: build a redirect root in app so we can maintain no ending slashes
)

# oh why oh why isn't there a REMOVE_SLASH option...
urlpatterns += patterns('',
    (r'^(?P<url>.*)$', 'views.remove_slash'),
)

