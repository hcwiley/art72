from models import ExtendedImage, Piece, Series, Category
from datetime import datetime
from portfolio import settings
from django.shortcuts import render_to_response, Http404, HttpResponse
#TODO: remove project dependency from app

def common_args(ajax=False):
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
               'base_template' : 'base.html',
           }
    if ajax:
        args['base_template'] = "base-ajax.html"
    return args 

def category(request, category):
    args = common_args()
    args['category'] = Category.objects.get(pk=category)
    return render_to_response('gallery/category.html', args)


def series(request, category, series):
    args = common_args()
    args['series'] = Series.objects.get(pk=series)
    return render_to_response('gallery/series.html', args)

def piece(request, category, series, piece):
    """
    #TODO: check that the category and series are correct
    Renders the home page.
    Context:
    """
    args = common_args()
    args['piece'] = Piece.objects.get(pk=piece)
    return render_to_response('gallery/piece.html', args )
