from django.conf import settings
from django.contrib import admin 
from django.contrib.auth import views as auth_views
from django.views.generic.simple import redirect_to, direct_to_template
from registration.views import activate, register
from registration.forms import RegistrationFormUniqueEmail
from django.conf.urls.defaults import patterns, include, url

#from art72_django.settings import DEBUG
#from art72_django.settings import AJAX_VIEW_PREFIX as ajax
admin.autodiscover()

# custom 404 and 500 handlers
handler404 = 'apps.promo.views.art72_404'
handler500 = 'apps.promo.views.art72_500'

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
                           {'template_name': 'promo/registration/login.html'},
                           name='auth_login'),
                       url(r'^accounts/logout$',
                           auth_views.logout,
                           {'template_name': 'promo/registration/logged_out.html'},
                           name='auth_logout'),
                       url(r'^accounts/register$',
                           register,
                           {'form_class':RegistrationFormUniqueEmail}, 
                           name='registration_register'),
                       url(r'^accounts/register/complete$',
                           direct_to_template,
                           {'template': 'promo/registration/registration_complete.html'},
                           name='registration_complete'),
                       )
#these forms needs to enforce the case insensitive email and username


if settings.DEBUG:
#     let us test out missing page and server error when debugging
#TODO don't let people name their top level series admin, site_media, etc.
    urlpatterns += patterns('',
        (r'^404$', handler404),
        (r'^500$', handler500),
	(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# public pages w/ajax support
urlpatterns += patterns('apps.promo.views',
    (r'^%s(?P<page>.*)$' % settings.AJAX_VIEW_PREFIX, 'ajax'),
    (r'^(?P<page>.*)$', 'default'),
#    (r'^(?P<ajax>(%s)?)contact$' % ajax, 'views.contact'),
)
