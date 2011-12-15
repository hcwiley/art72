from models import *
from datetime import datetime
from portfolio import settings
from django.shortcuts import render_to_response, Http404, HttpResponse
#TODO: remove project dependency from app

artist = Artist.objects.all()[0]

def common_args(request, ajax=False):
    """
    The common arguments for all gallery views.
    ajax: Describes if the args are for an ajax request.
    
    STATIC_URL: static url from settings
    year: the year at the time of request
    base_template: the default base template  
    """
    args = {
               'STATIC_URL' : settings.STATIC_URL,
               'year' : datetime.now().year,
               'theme' : Artist.objects.all()[0].get_theme(),
               'base_template' : 'base.html',
               'artist' : artist,
               'user' : request.user,
           }
    if ajax:
        args['base_template'] = "base-ajax.html"
    return args 

def home(request):
    args = common_args(request)
    args['categories'] = Category.objects.filter(artist=args['artist'])
    return render_to_response('gallery/gallery.html', args)

def category(request, category):
    args = common_args(request)
    args['category'] = Category.objects.get(pk=category)
    return render_to_response('gallery/category.html', args)

def series(request, category, series):
    args = common_args(request)
    args['series'] = Series.objects.get(pk=series)
    return render_to_response('gallery/series.html', args)

def piece(request, category, series, piece):
    """
    #TODO: check that the category and series are correct
    Renders the home page.
    Context:
    """
    args = common_args(request)
    args['piece'] = Piece.objects.get(pk=piece)
    return render_to_response('gallery/piece.html', args )
