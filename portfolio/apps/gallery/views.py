from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404, redirect
from apps.artist.models import Artist
from apps.gallery.models import Category, Series, Piece
from django.contrib.sites.models import Site
from django.views.generic.simple import redirect_to
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from django.template import loader
from django import http
from django.template.context import RequestContext, Context
from django.contrib.auth.decorators import login_required

# TODO: move back to /ajax/url - easy to block access that isn't coming internally and we won't get strange behaviour or full page loads needed over ajax
# TODO: move this to a context processor
def common_args(request):
    """
    The common arguments for all gallery views.
    
    STATIC_URL: static url from settings
    year: the year at the time of request  
    """ 
    artist = get_object_or_404(Artist, user__username=request.subdomain)
    args = {
                'base_template' : 'dashboard/base-ajax.html' if request.is_ajax() else 'dashboard/base.html',
                'artist' : artist,
                'STATIC_URL' : settings.STATIC_URL,
                'MEDIA_URL' : settings.MEDIA_URL,
                'theme' :  artist.theme,
           }
    return args
 
#TODO: user {% url %} tag in template for backwards lookup to view
def category(request, category):
    args = common_args(request)
    category = get_object_or_404(Category.gallery_objects, slug=category, artist=args['artist'])
    #Auto drill down to first page with content
#    if category.children().count() == 1:
#        return redirect('/gallery/%s/%s' % (category.slug, category.children().all()[0].slug))
    args['category'] = category
    return render_to_response('gallery/category.html', args)

def series(request, category, series):
    args = common_args(request)
    series = get_object_or_404(Series.gallery_objects, slug=series, artist=args['artist'])
    args['series'] = series
    #Auto drill down to first page with content
#    if series.children().count() == 1:
#        return redirect('/gallery/%s/%s/%s' % (series.category.slug, series.slug, series.children().all()[0].slug))
    return render_to_response('gallery/series.html', args)

def piece(request, category, series, piece):
    """
    #TODO: check that the category and series are correct, if not but it's found, redirect to the new url
    Renders the home page.
    Context:
    """
    args = common_args(request)
    args['piece'] = get_object_or_404(Piece.gallery_objects, slug=piece, artist=args['artist'])
    return render_to_response('gallery/piece.html', args )

def gallery(request):
    args = common_args(request)
    args['categories'] = Category.gallery_objects.filter(artist=args['artist'])
    return render_to_response('gallery/gallery.html', args)

# This can be called when CsrfViewMiddleware.process_view has not run, therefore
# need @requires_csrf_token in case the template needs {% csrf_token %}.
@requires_csrf_token
def gallery_404(request, template_name='gallery/404.html'):
    """ 
    404 handler for gallery sites.

    Templates: `404.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
        
    """
    if request.path.endswith('/'):
        return redirect_to(request, request.path.rstrip('/'))
    else:
        t = loader.get_template(template_name) # You need to create a 404.html template.
        args = common_args(request)
        args['request_path'] = request.path
        return http.HttpResponseNotFound(t.render(RequestContext(request, args)))

@requires_csrf_token
def gallery_500(request, template_name='gallery/500.html'):
    """ 
    500 error handler for gallery sites.

    Templates: `500.html`
    Context: common_args 
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return http.HttpResponseServerError(t.render(Context(common_args(request))))
