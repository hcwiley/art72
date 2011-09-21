from django.http import Http404
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.context_processors import *
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.forms import *
from piece.models import *
from artist.models import *
from contact_element.models import *
import os
from django.contrib.auth import *
from django.contrib import auth

def four_oh_four(request):
    return render_to_response('404.html', {'artist': Artist.objects.all()[0]})

def five_oh_oh(request):
    return render_to_response('500.html')

def contact(request):
    return render_to_response('contact.html', getBaseArgs())

def getSeries(ser):
    series = Series.objects.filter(slug=ser)[0] if len(Series.objects.filter(slug=ser)) > 0 else None
    pieces = series.piece_piece_series.all() if series is not None else None
    return pieces

def listSeries():
    sers = Series.objects.all()
    if len(sers) > 0:
        series = []
        for s in sers:
            series.append(s.name)
        return sers
    else:
        return None

base_args = {
           'serieses': listSeries(),
           'elements': ContactElement.objects.all(),
           'artist': Artist.objects.all()[0] if len(Artist.objects.all()) > 0 else Artist.objects.get_or_create(user=User.objects.all()[0]) 
}

def getBaseArgs():
    artist = Artist.objects.all()
    if len(artist) > 0:
        artist = artist[0]
    return {
           'serieses': listSeries(),
           'elements': ContactElement.objects.all(),
           'artist': artist
    }    

def index(request):
    args = getBaseArgs()
    args.update(csrf(request))
    return render_to_response('index.html', args)

def piece(request, series, slg = None):
    pieces = getSeries(series)
    if slg == None and pieces is not None:
        piece = pieces[0]
    else:
        afds
        raise Http404
    piece = Piece.objects.filter(slug = slg)[0] if len(Piece.objects.filter(slug = slg)) > 0 else None
    args = {
            'piece': piece,
            'pieces': pieces,
    }
    args.update(getBaseArgs())
    return render_to_response('piece.html', args)

def gallery(request, series):
    pieces = getSeries(series)
    args = {
        'pieces': pieces,
    }
    args.update(getBaseArgs())
    return render_to_response('gallery.html', args)

def get_page(request, page):
    #print page
    if page == 'edit':
        #print 'its the home page'
        args = getBaseArgs()
        args.update(csrf(request))
        return render_to_response('index_base.html', args)
    elif len(Piece.objects.filter(slug = page)) != 0:
        #print 'its a piece page some how'
        piece = Piece.objects.filter(slug = page)[0]
        pieces = getSeries(Piece.objects.filter(slug = page)[0].series.all()[0].slug)
    else:
        #print 'its a gallery'
        pieces = getSeries(page)
        piece = pieces[0] if pieces is not None else None
    #print piece
    #print pieces
    args = {
            'piece': piece,
            'pieces': pieces,
    }
    args.update(getBaseArgs())
    return render_to_response('piece_base.html', args)

def get_header(request):
    args = getBaseArgs()
    return render_to_response('edit_header.html', args)

def edit_index(request):
    if request.user.is_authenticated():
        args = {
           'piece_form': PieceForm(auto_id = 'piece_%s'),
           'series_form': SeriesForm(auto_id = 'series_%s'),
           'user': request.user,
        }
        args.update(getBaseArgs())
        args.update(csrf(request))
        return render_to_response('edit_index.html', args)
    else:
        args = {
           'user': request.user,
    }
    args.update(getBaseArgs())
    args.update(csrf(request))
    return render_to_response('edit_index.html', args)

def edit_contact(request):
    if request.user.is_authenticated():
        args = { 'user': request.user,
                 'ce_form': ContactElementForm(auto_id = 'ce_form_%s'),
                 }
        args.update(getBaseArgs())
        return render_to_response('edit_contact.html', args)
    else:
        args = {
           'user': request.user,
    }
    args.update(getBaseArgs())
    args.update(csrf(request))
    return render_to_response('edit_index.html', args)

def edit_piece(request, series, slg = None):
    if request.user.is_authenticated():
        pieces = getSeries(series)
        if slg == None:
            if len(pieces) != 0:
                piece = pieces[0]
            else:
                piece = None
        else:
            piece = Piece.objects.filter(slug = slg)[0] if len(Piece.objects.filter(slug=slg)) > 0 else None
        args = {
                'piece': piece,
                'pieces': pieces,
                'piece_form': PieceForm(auto_id = 'piece_%s'),
                'series_form': SeriesForm(auto_id = 'series_%s'),
                'user': request.user,
                }
        args.update(getBaseArgs())
        args.update(csrf(request))
        return render_to_response('edit_piece.html', args)
    else:
        args = {
           'user': request.user,
    }
    args.update(getBaseArgs())
    args.update(csrf(request))
    return render_to_response('edit_index.html', args)

def edit_gallery(request, series):
    if request.user.is_authenticated():
        pieces = getSeries(series)
        args = {
                'pieces': pieces,
                'piece_form': PieceForm(auto_id = 'piece_%s'),
                'series_form': SeriesForm(auto_id = 'series_%s'),
                'user': request.user,
        }
        args.update(getBaseArgs())
        args.update(csrf(request))
        return render_to_response('edit_gallery.html', args)
    else:
        args = {
           'user': request.user,
    }
    args.update(getBaseArgs())
    args.update(csrf(request))
    return render_to_response('edit_index.html', args)

def add_piece(request):
    if request.method != "POST":
        raise Http404
    form = PieceForm(request.POST, request.FILES)
    if form.is_valid():
        #print 'good form'
        title = form.cleaned_data['title']
        img = request.FILES['default_image']
        img = MyImage.objects.get_or_create(image=img)[0]
        date = form.cleaned_data['date']
        price = form.cleaned_data['price']
        ser = form.cleaned_data['series']
        #print 'got all the form data'
        series = Series.objects.get_or_create(slug=slugify(ser))[0]
        series.name = ser
        series.save()
        #print 'series is good'
        obj = Piece.objects.get_or_create(slug=slugify(title))[0]
        #print 'made an object?'
        obj.title = title
        obj.default_image = img
        obj.date = date
        obj.price = price
        obj.series = [series]
        obj.save()
        #print 'you rule!'
        return HttpResponse("success")
    else:
        #print 'bad form'
        return HttpResponse("invalid form")

def add_series(request):
    if request.method != "POST":
        raise Http404
    form = SeriesForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        des = form.cleaned_data['description']
        if len(Series.objects.filter(slug=slugify(name))) == 0:
            ser = Series.objects.create()
            ser.name = name
            #print ser
            ser.description = des
            ser.save()
            return HttpResponse("success")
        else:
            #print 'series already exist'
            return HttpResponse("series already exist")
    else:
        #print 'bad form'
        return HttpResponseNotFound("invalid form")

def save_css(request, id):
    if request.method != "POST":
        raise Http404
#    #print request.POST
    form = CssForm(request.POST)
    #print form
    if form.is_valid():
        os.system('cp ../public/css/template2.css ../public/css/template2.css.bak')
        cssNew = open('../public/css/template2.css.new', 'w+')
        cssOrig = open('../public/css/template2.css', 'r')
        add = False
        section = []
        #print id
        for line in cssOrig:
            if '#%s {' % id in line or '#%s{' % id in line:
                add = True
            if add:
                if 'width' in line and id != 'nav':
                    line = '    width: %dpx;\n' % form.cleaned_data['width']
                    #print 'fixed width'
                if 'height' in line and id != 'nav':
                    line = '    height: %dpx;\n' % form.cleaned_data['height']
                    #print 'fixed height'
                if 'top' in line:
                    line = '    top: %dpx;\n' % form.cleaned_data['top']
                    #print 'fixed top'
                if 'left' in line:
                    line = '    left: %dpx;\n' % form.cleaned_data['left']
                    #print 'fixed left'
            if '}' in line:
                add = False
            cssNew.write(line)
        cssNew.flush()
        cssNew.close()
        cssOrig.close()
        os.system('cp ../public/css/template2.css.new ../public/css/template2.css')
        return HttpResponse("success")
    else:
        #print 'bad css form'
        return HttpResponseNotFound("invalid form")

def draft_css(request, id):
    if request.method != "POST":
        raise Http404
#    #print request.POST
    form = CssForm(request.POST)
    #print form
    if form.is_valid():
        os.system('cp ../public/css/template2.css ../public/css/template2.css.bak')
        cssNew = open('../public/css/template2.draft.css', 'w+')
        cssOrig = open('../public/css/template2.css', 'r')
        add = False
        section = []
        #print id
        for line in cssOrig:
            if '#%s {' % id in line or '#%s{' % id in line:
                add = True
            if add:
                if 'width' in line and id != 'nav':
                    line = '    width: %dpx;\n' % form.cleaned_data['width']
                    #print 'fixed width'
                if 'height' in line and id != 'nav':
                    line = '    height: %dpx;\n' % form.cleaned_data['height']
                    #print 'fixed height'
                if 'top' in line:
                    line = '    top: %dpx;\n' % form.cleaned_data['top']
                    #print 'fixed top'
                if 'left' in line:
                    line = '    left: %dpx;\n' % form.cleaned_data['left']
                    #print 'fixed left'
            if '}' in line:
                add = False
            cssNew.write(line)
        cssNew.flush()
        cssNew.close()
        cssOrig.close()
        return HttpResponse("success")
    else:
        #print 'bad css form'
        return HttpResponseNotFound("invalid form")

def save_logo(request):
    if request.method != "POST":
        raise Http404
    logo = request.POST['logo']
    artist = request.POST['user']
    artist = User.objects.filter(username=artist)[0]
    artist = Artist.objects.filter(user=artist)[0]
    if artist != None:
        #print artist.site_name
        artist.site_name = logo
        #print artist.site_name
        artist.save()
        return HttpResponse("success")
    else:
        return HttpResponseNotFound("user not found")

def update_contact(request):
    if request.method != "POST":
        raise Http404
    dis = request.POST['displayed']
    type = request.POST['type']
    link = request.POST['link']
    artist = request.POST['user']
    artist = User.objects.filter(username=artist)[0]
    artist = Artist.objects.filter(user=artist)[0]
#    if request.FILES['file'] != None:
#        file = request.FILES['file']
    if artist != None:
        contact = ContactElement.objects.get_or_create(displayed=dis)[0]
        contact.type = type
        contact.links_to = link
        contact.save()
        return HttpResponse("success")
    else:
        return HttpResponseNotFound("user not found")

def login(request):
    usern = request.POST['username']
    passw = request.POST['password']
    #print usern
    #print passw
    user = auth.authenticate(username = usern, password = passw)
    #print user
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponse("success")
    else:
        # Show an error page
        #print 'nope'
        return HttpResponse('failed')
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("success")

def add_video(request):
    if request.method != "POST":
        raise Http404
    form = VideoLinkForm(request.POST)
    if form.is_valid():
        return_text = 'added'
        title = form.cleaned_data['title']
        url = form.cleaned_data['url']
        obj = VideoLink.objects.get_or_create(slug=slugify(title))
        if obj[1] == 1:
            return_text = 'updated'
        obj = obj[0]
        obj.title= title
        obj.url = url
        obj.save()
        return HttpResponse('successfully %: %s' % (return_text, title))
    else:
        return HttpResponse('failed to add: %s @ %s' % (title, url)) 

def add_video_user(request):
    if request.method != "POST":
        raise Http404
    form = VideoUserForm(request.POST)
    if form.is_valid():
        return_text = 'added'
        username = form.cleaned_data['username']
        url = form.cleaned_data['url']
        typ = form.cleaned_data['type']
        obj = VideoUser.objects.get_or_create(slug=slugify(username),type=typ)
        print obj
        if obj[1] == 1:
            return_text = 'updated'
        obj = obj[0]
        obj.username= username
        obj.url = url
        obj.type = typ
        obj.save()
        return HttpResponse('successfully %: %s' % (return_text, title))
    else:
        return HttpResponse('failed to add: %s @ %s' % (title, url)) 

def video(request):
    args = getBaseArgs()
    args['user']= request.user
    args['videos'] = VideoLink.objects.all()
    args['video_user_form'] = VideoUserForm(auto_id = 'video_user_%s')
    args.update(csrf(request))
    return render_to_response('video.html', args)