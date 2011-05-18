from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.context_processors import csrf
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import SimpleUploadedFile
from piece.models import *

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
    series = Series.objects.filter(slug=ser)[0]
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
            'piece': Piece.objects.filter(slug=slg)[0],
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

def get_header(request):
    args = {
            'serieses': listSeries()
            }
    return render_to_response('header.html', args)

def edit_index(request):
    args = {
           'serieses': listSeries(),
           'piece_form': PieceForm(auto_id='piece_%s'),
    }
    args.update(csrf(request))
    return render_to_response('edit_index.html', args)

def edit_contact(request):
    return render_to_response('edit_contact.html', {'serieses': listSeries()})

def edit_piece(request, series, slg):
    pieces = getSeries(series)
    args = {
            'piece': Piece.objects.filter(slug=slg)[0],
            'pieces': pieces,
            'serieses': listSeries(),
            'piece_form': PieceForm(auto_id='piece_%s'),
            }
    args.update(csrf(request))
    return render_to_response('edit_piece.html', args) 

def edit_gallery(request, series):
    pieces = getSeries(series)
    args = {
            'pieces': pieces,
            'serieses': listSeries(),
            'piece_form': PieceForm(auto_id='piece_%s'),
    }
    args.update(csrf(request))
    return render_to_response('edit_gallery.html', args)

def add_piece(request):
    if request.method != "POST":
        raise Http404
    form = PieceForm(request.POST, request.FILES)
    print "files", request.FILES
    if form.is_valid():
        title = form.cleaned_data['title']
#        handle_uploaded_file(request.FILES['default_image'])
        img = request.FILES['default_image']
        img = Image.objects.get_or_create(image=img)[0]
        print 'image %s' % img
        date = form.cleaned_data['date']
        price = form.cleaned_data['price']
        ser = form.cleaned_data['series']
        series = Series.objects.get_or_create(slug=slugify(ser))[0]
        series.name = ser
        series.save()
        
        obj = Piece.objects.get_or_create(slug=slugify(title))[0]
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

def handle_uploaded_file(f):
    # DRY violation, I've already specified the upload path in the image model
    print 'yes?'
    path = 'gallery/%s' % f.name
    print path
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
