from django.conf.urls import patterns, include, url
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello, Mark</h1>')

urlpatterns = patterns('',  
    url(r'^$', hello),
)
