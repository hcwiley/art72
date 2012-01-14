from datetime import datetime
from django import http
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response, Http404, HttpResponse
from django.template import Context, Template, RequestContext, loader
from django.views.generic.simple import redirect_to
from django.views.decorators.csrf import requires_csrf_token
#from biz.models import BusinessDetail, Association, Service, Link
from apps.contactform.utils import submit as submit_contact_form
import settings

pages = ['home', 'features', 'signup', 'pricing', 'register']

def common_args(ajax=False):
    """
    The common arguments for all art72_django views.
    ajax: Describes if the args are for an ajax request.
    
    STATIC_URL: static url from settings
    year: the year at the time of request
    contact: art72_django business contact information
    base_template: the default base template  
    """
    args = {
               'STATIC_URL' : settings.STATIC_URL,
               'year' : datetime.now().year,
               'base_template' : 'promo/base.html',
           }
    if ajax:
        args['base_template'] = "promo/base-ajax.html"
    return args 
    
# This can be called when CsrfViewMiddleware.process_view has not run, therefore
# need @requires_csrf_token in case the template needs {% csrf_token %}.
@requires_csrf_token
def art72_django(request, template_name='common/404.html'):
    """ 
    404 handler for art72_django.

    Templates: `404.html`
    Context:
        common_args from art72_django
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
        
    """
    t = loader.get_template(template_name) # You need to create a 404.html template.
    args = common_args()
    args['request_path'] = request.path
    return http.HttpResponseNotFound(t.render(RequestContext(request, args)))

@requires_csrf_token
def art72_django_500(request, template_name='500.html'):
    """ 
    500 error handler for art72_django.

    Templates: `500.html`
    Context: common_args from art72_django
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return http.HttpResponseServerError(t.render(Context(common_args())))

def default(request, page):
    args = common_args(False)
    args.update(csrf(request))
    if page == '':
        page = 'home'
    if page in pages:
        args['page'] = page
        return render_to_response('promo/%s.html' % page, args)
    else:
        raise Http404
    
def ajax(request, page):
    print 'ajax'
    args = common_args(True)
    args.update(csrf(request))
    if page == '' or page == '/' :
        page = 'home'
    if page in pages:
        return render_to_response('promo/%s.html' % page, args)
    else:
        raise Http404

 
def home(request, ajax):
    """
    Renders the home page.
    Context:
        common args
        assocs - list of all professional associations
    """
    args = common_args(ajax)
    args.update(csrf(request))
    return render_to_response('promo/home.html', args)

def features(request, ajax):
    """
    Renders the home page.
    Context:
        common args
        assocs - list of all professional associations
    """
    args = common_args(ajax)
    args.update(csrf(request))
    return render_to_response('promo/features.html', args)

def signup(request, ajax):
    """
    Renders the signup page.
    Context:
        common args
    """
    args = common_args(ajax)
    args.update(csrf(request))
    return render_to_response('promo/signup.html', args)

def features(request, ajax):
    """
    Renders the pricing page.
    Context:
        common args
    """
    args = common_args(ajax)
    args.update(csrf(request))
    return render_to_response('promo/pricing.html', args)

def email_signup(request):
    recipients = ['decode72@decode72.com']
    args = common_args(True)
    submit_results = submit_contact_form(request, recipients, settings.DEBUG, redirect_url='/contact')
    return HttpResponse(submit_results['message'])
#    print submit_results
#    args.update(submit_results)
#    print 'updated args'
#    return render_to_response('.html', args)


def remove_slash(request, url):
    """
    Rechecks the URL without the trailing slash(es) before raising an Http404.
    TODO: look into moving this into the custom 404 handler - won't need have a catchall url this way.
    """
    if url.endswith('/'):
        return redirect_to(request, '/' + url.rstrip('/'))
    else:
        raise Http404
    
def admin_add_slash(request):
    """
    Because APPEND_SLASH is false, manually append slash in this case.
    """
    return redirect_to(request, request.path + '/')
