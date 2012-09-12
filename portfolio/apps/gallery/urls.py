from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import redirect_to, direct_to_template
from django.conf.urls.defaults import patterns, url, include
from django.contrib.auth import views as auth_views
admin.autodiscover()

# custom 404 and 500 handlers
handler404 = 'apps.gallery.views.gallery_404'
handler500 = 'apps.gallery.views.gallery_500'

# basic stuff
urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
)

if settings.DEBUG:
    # let django serve user generated media while in development
    urlpatterns += patterns('',
#TODO don't let people name their top level series admin, site_media, etc.
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^404$', handler404),
        (r'^500$', handler500),
    )

# main gallery views
urlpatterns += patterns('apps.gallery.views',
    (r'^gallery/(?P<category>[^/]+)/(?P<series>[^/]+)/(?P<piece>[^/]+)$', 'piece'),
    (r'^gallery/(?P<category>[^/]+)/(?P<series>[^/]+)$', 'series'),
    (r'^gallery/(?P<category>[^/]+)$', 'category'),
    (r'^gallery$', 'gallery'),
    (r'^$', redirect_to, {'url': '/gallery'}),
)

# secondary gallery views
urlpatterns += patterns('apps.gallery.views',
#    (r'^contact$', 'contact'),
)

# dashboard views
urlpatterns += patterns('',
    #TODO: this is a hack to allow for no slashes... dashboard urls start with slash, except for the home one
    (r'^dashboard', include('apps.dashboard.urls')),                       
)

# login
urlpatterns += patterns('',
                        url(r'^accounts/login$',
                           auth_views.login,
                           {'template_name': 'promo/registration/login.html'},
                           name='auth_login'),
                       url(r'^accounts/logout$',
                           auth_views.logout,
                           {'template_name': 'promo/registration/logged_out.html'},
                           name='auth_logout'),
                        )
#TODO: make these login/logout auth_views not user the trailing slash so they don't redirect every single time

# ajax service calls
urlpatterns += patterns('apps.gallery.views',
)
