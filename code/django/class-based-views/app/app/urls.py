from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import TemplateView

admin.autodiscover()

from app.views import ContactList

def hello(request):
    return HttpResponse('<h1>Hello, Mark</h1>')

urlpatterns = patterns('',  
    url(r'^$', hello),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
    url(r'^contacts/$', ContactList.as_view()),
)
