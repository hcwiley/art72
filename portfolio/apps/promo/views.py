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

pages = ['home', 'features', 'signup', 'pricing', 'register', 'terms']

def common_args(ajax=False):
    """
    The common arguments for all art72_django views.
    ajax: Describes if the args are for an ajax request.
    
    contact: art72_django business contact information
    base_template: the default base template  
    """
    args = {
               'base_template' : 'promo/base.html',
           }
    if ajax:
        args['base_template'] = "promo/base-ajax.html"
    return args 
    
# This can be called when CsrfViewMiddleware.process_view has not run, therefore
# need @requires_csrf_token in case the template needs {% csrf_token %}.
@requires_csrf_token
def art72_404(request, template_name='promo/common/404.html'):
    """ 
    404 handler for art72 promo site.

    Templates: `404.html`
    Context:
        common_args from art72_django
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
        
    """
    if request.path.endswith('/'):
        return redirect_to(request, request.path.rstrip('/'))
    elif request.path == '/admin':
        return redirect_to(request, '/admin/')
    else:
        t = loader.get_template(template_name) # You need to create a 404.html template.
        args = common_args()
        args['request_path'] = request.path
        return http.HttpResponseNotFound(t.render(RequestContext(request, args)))

@requires_csrf_token
def art72_500(request, template_name='promo/common/500.html'):
    """ 
    500 error handler for art72 promo site.

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
        return render_to_response('promo/%s.html' % page, args, context_instance=RequestContext(request))
    else:
        raise Http404
    
def ajax(request, page):
    args = common_args(True)
    args.update(csrf(request))
    if page == '' or page == '/' :
        page = 'home'
    if page in pages:
        return render_to_response('promo/%s.html' % page, args, context_instance=RequestContext(request))
    else:
        raise Http404

def email_signup(request):
    recipients = ['decode72@decode72.com']
    args = common_args(True)
    submit_results = submit_contact_form(request, recipients, settings.DEBUG, redirect_url='/contact')
    return HttpResponse(submit_results['message'])
#    print submit_results
#    args.update(submit_results)
#    print 'updated args'
#    return render_to_response('.html', args)
