from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from contact.models import Contact
from django.core import serializers

def add_contact():
    c = Contact()
    c.name = 'me'
    c.address  = 'here'
    c.phone = '42'
    c.save()


def add_view(request):
    add_contact()
    contacts = ','.join([c.name for c in Contact.objects.all()])
    return HttpResponse('<h1>Contact added</h1>'+\
                        '<p>'+contacts+'</p>')

def json_view(request):
    c = Contact.objects.all()[0]
    j = serializers.serialize("json", c)
    print j
    return HttpResponse('<h1>JSON view</h1>'+\
                        '<p>'+j+'</p>')

urlpatterns = patterns('',  
    url(r'^$', add_view),
    url(r'^json$',json_view),
)


