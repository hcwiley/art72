from django.shortcuts import render_to_response, Http404
from django.views.generic.simple import redirect_to
from gallery.models import ExtendedImage, Piece, Category

def home(request):
    """
    Renders the home page.
    Context:
    """
    return render_to_response('index.html', {'categories': Catergory.objects.all() })
   
def remove_slash(request, url):
    """
    Rechecks the URL without the trailing slash(es) before raising an Http404.
    TODO: look into moving this into the custom 404 handler - won't need have a catchall url this way.
    """
    print 'uh oh'
    if url.endswith('/'):
        return redirect_to(request, '/' + url.rstrip('/'))
    else:
        raise Http404
    
def admin_add_slash(request):
    """
    Because APPEND_SLASH is false, manually append slash in this case.
    """
    return redirect_to(request, request.path + '/')
