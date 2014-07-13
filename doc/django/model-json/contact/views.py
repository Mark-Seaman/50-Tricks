from django.http import HttpResponse
from contact.models import Contact
from django.core import serializers


# Render a view
def hello(request):
    return HttpResponse('<h1>JSON Web Service Demo</h1>'+\
                        '<p>Show how to list JSON for lists of objects.</p>'+\
                        '<p>Handle posts of updates from UI.</p>')


# Return a list as JSON
def json_list(request):
    data = serializers.serialize("json", Contact.objects.all())
    return HttpResponse('List = '+data)


# Return a list as JSON
def json_post(request):
    data = request
    print data
    return HttpResponse('OK')
