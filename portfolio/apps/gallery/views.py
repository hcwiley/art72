from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from artist.models import Artist
from gallery.models import Category, Series, Piece

def common_args(request, artist):
    """
    The common arguments for all gallery views.
    
    STATIC_URL: static url from settings
    year: the year at the time of request  
    """ 
    
    args = {
               'STATIC_URL' : settings.STATIC_URL,
               'year' : datetime.now().year,
               'user' : request.user,
               'artist' : get_object_or_404(Artist, user__username=artist), 
           }
    return args 
#TODO: user {% url %} tag in template for backwards lookup to view
def category(request, artist, category):
    args = common_args(request, artist)
    args['category'] = get_object_or_404(Category, pk=category)
    return render_to_response('gallery/category.html', args)

def series(request, artist, category, series):
    args = common_args(request, artist)
    args['series'] = get_object_or_404(Series, pk=series)
    return render_to_response('gallery/series.html', args)

def piece(request, artist, category, series, piece):
    """
    #TODO: check that the category and series are correct
    Renders the home page.
    Context:
    """
    args = common_args(request, artist)
    args['piece'] = get_object_or_404(Piece, pk=piece)
    return render_to_response('gallery/piece.html', args )

def artist(request, artist):
    args = common_args(request, artist)
    args['categories'] = args['artist'].category_set.all()
    return render_to_response('gallery/gallery.html', args)
