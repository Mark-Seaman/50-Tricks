from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello-World</h1>'+\
                        '<p>/home/seaman/Projects/tricks/code/django/hello-world/app/app</p>')
