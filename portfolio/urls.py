from django.conf import settings
from django.contrib import admin 
from django.contrib.auth import views as auth_views
from django.views.generic.simple import redirect_to, direct_to_template
from gallery import urls as gallery_urls
from django.conf.urls.defaults import patterns, include, url
from registration.views import activate
from registration.views import register
from registration.forms import RegistrationFormUniqueEmail
admin.autodiscover()

# basic stuff
urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin$', 'views.admin_add_slash'),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
)

#urlpatterns += patterns('',
#    (r'^accounts/login$',  auth_views.login),
#    (r'^accounts/logout$', auth_views.logout),
#)

urlpatterns += patterns('',
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^accounts/activate/(?P<activation_key>\w+)$',
                           activate,
                           name='registration_activate'),
                       url(r'^accounts/login$',
                           auth_views.login,
                           {'template_name': 'registration/login.html'},
                           name='auth_login'),
                       url(r'^accounts/logout$',
                           auth_views.logout,
                           {'template_name': 'registration/logged_out.html'},
                           name='auth_logout'),
                       url(r'^accounts/register$',
                           register,
                           {'form_class':RegistrationFormUniqueEmail}, 
                           name='registration_register'),
                       url(r'^accounts/register/complete$',
                           direct_to_template,
                           {'template': 'registration/registration_complete.html'},
                           name='registration_complete'),
                       )


if settings.DEBUG:
    # let django serve user generated media while in development
    urlpatterns += patterns('',
#TODO don't let people name their top level series admin, site_media, etc.
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    (r'^$', 'views.welcome'),
    (r'^', include(gallery_urls)),
)

# oh why oh why isn't there a REMOVE_SLASH option...
urlpatterns += patterns('',
    (r'^(?P<url>.*)$', 'views.remove_slash'),
)

