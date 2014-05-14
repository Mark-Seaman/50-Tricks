from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.views.generic import TemplateView


# Hard-coded HTML
def hello(request):
    return HttpResponse('<h1>Template View Demo</h1><a href="about">About</a>')


# Web page routing
urlpatterns = patterns('',  
    url(r'^$', hello),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
)
