from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

def hello(request):
    return HttpResponse('<h1>Hello, Mark</h1>')

urlpatterns = patterns('',  
    url(r'^$', hello),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
)
