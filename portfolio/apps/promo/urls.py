from django.conf import settings
from django.contrib import admin 
from django.contrib.auth import views as auth_views
from django.views.generic.simple import redirect_to, direct_to_template
from django.conf.urls.defaults import patterns, include, url
from registration.views import activate, register
from registration.forms import RegistrationFormUniqueEmail
from django.conf.urls.defaults import *
from django.contrib import admin 
from apps.promo import views as promo_views
from django.views.generic.simple import redirect_to, direct_to_template

#from art72_django.settings import DEBUG
#from art72_django.settings import AJAX_VIEW_PREFIX as ajax
admin.autodiscover()

# custom 404 and 500 handlers
handler404 = 'views.art72_django'
handler500 = 'views.art72_django_500'

# basic stuff
urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
#    (r'^email-signup$', 'views.email_signup'),
)

#TODO: submit a pull request to sorl thumbnail with updated django admin docs entry
#TODO: allow login via username or email
#TODO: make username and email unique check case insensitive
#TODO: figure out what characters will be allowed for usernames
#TODO: add in site domain info to email templates so activation links can go out correctly for testing
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
#these forms needs to enforce the case insensitive email and username

# public pages w/ajax support
urlpatterns += patterns('promo.views',
    (r'^%s(?P<page>.*)$' % settings.AJAX_VIEW_PREFIX, 'ajax'),
    (r'^(?P<page>.*)$', 'default'),
#    (r'^(?P<ajax>(%s)?)contact$' % ajax, 'views.contact'),
)

if settings.DEBUG:
#     let us test out missing page and server error when debugging
#TODO don't let people name their top level series admin, site_media, etc.
    urlpatterns += patterns('',
#        (r'^404$', 'views.art72_django'),
#        (r'^500$', 'views.art72_django_500'),
	(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# oh why oh why isn't there a REMOVE_SLASH option...
urlpatterns += patterns('',
    (r'^admin$', 'views.admin_add_slash'),
    (r'^(?P<url>.*)$', 'views.remove_slash'),
)

