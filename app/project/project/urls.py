# urls.py
# Simple page showing how to load twitter bootstrap

from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.template import loader,Context

from settings import STATIC_ROOT

# Define the location of the static files
static_dir   = { 'document_root' : STATIC_ROOT}


# Create a page with a template
def home(request): 
    page = loader.get_template ('home.html')
    return HttpResponse(page.render(Context({})))


# Routes to the views
urlpatterns = patterns('',  

    # static files
    url(r'^static/(?P<path>.*)$',    'django.views.static.serve', static_dir),

    # show the default page
    url(r'^$', home),

)
