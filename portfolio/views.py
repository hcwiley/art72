from django.contrib.sites.models import Site
from django.shortcuts import Http404, render_to_response
from django.views.generic.simple import redirect_to
from artist.models import Artist
   
def welcome(request):
    if request.user.is_authenticated():
        user = request.user
        domain = Site.objects.get_current().domain
        return render_to_response('registration/profile.html', locals())
    else:
        return render_to_response('welcome.html', {'artists': Artist.objects.all()})
   
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
