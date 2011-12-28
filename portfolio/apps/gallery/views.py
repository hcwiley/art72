from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from artist.models import Artist
from gallery.models import Category, Series, Piece

def common_args(request):
    """
    The common arguments for all gallery views.
    
    STATIC_URL: static url from settings
    year: the year at the time of request  
    """ 
    
    args = {
               'STATIC_URL' : settings.STATIC_URL,
               'year' : datetime.now().year,
               'user' : request.user,
               'artist' : get_object_or_404(Artist, user__username=request.subdomain), 
           }
    return args 
#TODO: user {% url %} tag in template for backwards lookup to view
def category(request, category):
    args = common_args(request)
    args['category'] = get_object_or_404(Category, slug=category)
    return render_to_response('gallery/category.html', args)

def series(request, category, series):
    args = common_args(request)
    args['series'] = get_object_or_404(Series, slug=series)
    return render_to_response('gallery/series.html', args)

def piece(request, category, series, piece):
    """
    #TODO: check that the category and series are correct
    Renders the home page.
    Context:
    """
    args = common_args(request)
    args['piece'] = get_object_or_404(Piece, slug=piece)
    return render_to_response('gallery/piece.html', args )

def artist(request):
    args = common_args(request)
    args['categories'] = args['artist'].category_set.all()
    return render_to_response('gallery/gallery.html', args)
