from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.context_processors import csrf
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.forms import *
from piece.models import *
import os

#mediums = (
#           'painting',
#           'sculpture',
#           'photography',
#           'installation',
#           'visualizations',
#           )

def contact(request):
    return render_to_response('contact.html', {'serieses': listSeries()})

def getSeries(ser):
    series = Series.objects.filter(slug = ser)[0]
    pieces = series.piece_piece_series.all()
    return pieces

def listSeries():
    sers = Series.objects.all()
    series = []
    for s in sers:
        series.append(s.name)
    return sers

def index(request):
    args = {
           'serieses': listSeries()
    }
    args.update(csrf(request))
    return render_to_response('index.html', args)

def piece(request, series, slg):
    pieces = getSeries(series)
    args = {
            'piece': Piece.objects.filter(slug = slg)[0],
            'pieces': pieces,
            'serieses': listSeries()
            }
    return render_to_response('piece.html', args)

def gallery(request, series):
    pieces = getSeries(series)
    args = {
            'pieces': pieces,
            'serieses': listSeries()
    }
    return render_to_response('gallery.html', args)

def get_page(request, page):
    print 'getting page: %s' %page
    if len(Piece.objects.filter(slug=page)) != 0:
        print 'its piece page'
        pieces = getSeries(Piece.objects.filter(slug=page)[0].series.all()[0].slug)
        print pieces
        args = {
                'piece': Piece.objects.filter(slug=page)[0],
                'pieces': pieces,
                'serieses': listSeries()
                }
        return render_to_response('piece_base.html', args)
    elif len(Series.objects.filter(slug=page)) != 0:
        print 'its gallery page'
        pieces = getSeries(page)
        args = {
                'pieces': pieces,
                'serieses': listSeries()
        }
        return render_to_response('gallery_base.html', args)
    else:
        print 'well fuck...'
        return HttpResponseNotFound("couldn't find it")

def get_header(request):
    args = {
            'serieses': listSeries()
            }
    return render_to_response('header.html', args)

def edit_index(request):
    args = {
           'serieses': listSeries(),
           'piece_form': PieceForm(auto_id = 'piece_%s'),
    }
    args.update(csrf(request))
    return render_to_response('edit_index.html', args)

def edit_contact(request):
    return render_to_response('edit_contact.html', {'serieses': listSeries()})

def edit_piece(request, series, slg):
    pieces = getSeries(series)
    args = {
            'piece': Piece.objects.filter(slug = slg)[0],
            'pieces': pieces,
            'serieses': listSeries(),
            'piece_form': PieceForm(auto_id = 'piece_%s'),
            }
    args.update(csrf(request))
    return render_to_response('edit_piece.html', args)

def edit_gallery(request, series):
    pieces = getSeries(series)
    args = {
            'pieces': pieces,
            'serieses': listSeries(),
            'piece_form': PieceForm(auto_id = 'piece_%s'),
    }
    args.update(csrf(request))
    return render_to_response('edit_gallery.html', args)

def add_piece(request):
    if request.method != "POST":
        raise Http404
    form = PieceForm(request.POST, request.FILES)
    if form.is_valid():
        title = form.cleaned_data['title']
        img = request.FILES['default_image']
        img = Image.objects.get_or_create(image = img)[0]
        date = form.cleaned_data['date']
        price = form.cleaned_data['price']
        ser = form.cleaned_data['series']
        series = Series.objects.get_or_create(slug = slugify(ser))[0]
        series.name = ser
        series.save()

        obj = Piece.objects.get_or_create(slug = slugify(title))[0]
        obj.title = title
        obj.default_image = img
        obj.date = date
        obj.price = price
        obj.series = [series]

        obj.save()

        return HttpResponse("success")
    else:
        print 'bad form'
        return HttpResponseNotFound("invalid form")

def save_css(request, id):
    if request.method != "POST":
        raise Http404
#    print request.POST
    form = CssForm(request.POST)
    print form
    if form.is_valid():
        os.system('cp ../public/css/template2.css ../public/css/template2.css.bak')
        cssNew = open('../public/css/template2.css.new', 'w+')
        cssOrig = open('../public/css/template2.css', 'r')
        add = False
        section = []
        print id
        for line in cssOrig:
            if '#%s {' % id in line or '#%s{' % id in line:
                add = True
            if add:
                if 'width' in line and id != 'nav':
                    line = '    width: %dpx;\n' % form.cleaned_data['width']
                    print 'fixed width'
                if 'height' in line and id != 'nav':
                    line = '    height: %dpx;\n' % form.cleaned_data['height']
                    print 'fixed height'
                if 'top' in line:
                    line = '    top: %dpx;\n' % form.cleaned_data['top']
                    print 'fixed top'
                if 'left' in line:
                    line = '    left: %dpx;\n' % form.cleaned_data['left']
                    print 'fixed left'
            if '}' in line:
                add = False
            cssNew.write(line)
        cssNew.flush()
        cssNew.close()
        cssOrig.close()
        os.system('cp ../public/css/template2.css.new ../public/css/template2.css')
        return HttpResponse("success")
    else:
        print 'bad css form'
        return HttpResponseNotFound("invalid form")

def draft_css(request, id):
    if request.method != "POST":
        raise Http404
#    print request.POST
    form = CssForm(request.POST)
    print form
    if form.is_valid():
        os.system('cp ../public/css/template2.css ../public/css/template2.css.bak')
        cssNew = open('../public/css/template2.draft.css', 'w+')
        cssOrig = open('../public/css/template2.css', 'r')
        add = False
        section = []
        print id
        for line in cssOrig:
            if '#%s {' % id in line or '#%s{' % id in line:
                add = True
            if add:
                if 'width' in line and id != 'nav':
                    line = '    width: %dpx;\n' % form.cleaned_data['width']
                    print 'fixed width'
                if 'height' in line and id != 'nav':
                    line = '    height: %dpx;\n' % form.cleaned_data['height']
                    print 'fixed height'
                if 'top' in line:
                    line = '    top: %dpx;\n' % form.cleaned_data['top']
                    print 'fixed top'
                if 'left' in line:
                    line = '    left: %dpx;\n' % form.cleaned_data['left']
                    print 'fixed left'
            if '}' in line:
                add = False
            cssNew.write(line)
        cssNew.flush()
        cssNew.close()
        cssOrig.close()
        return HttpResponse("success")
    else:
        print 'bad css form'
        return HttpResponseNotFound("invalid form")