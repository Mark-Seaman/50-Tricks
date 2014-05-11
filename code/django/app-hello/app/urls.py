from django.conf.urls import patterns, include, url
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello-World</h1>'+\
                        '<p>/home/seaman/Projects/tricks/code/django/hello-world/app/app</p>')

urlpatterns = patterns('',  
    url(r'^$', hello),
)
