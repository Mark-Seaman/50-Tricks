from django.conf.urls import patterns, include, url
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello There</h1><a href="/">About</a>')

urlpatterns = patterns('',  
    url(r'^$', hello),
)
