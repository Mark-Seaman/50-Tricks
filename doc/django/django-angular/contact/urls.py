from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',  

    url(r'^$',     'contact.views.hello'),
    url(r'^list$', 'contact.views.json_list'),
    url(r'^put$',  'contact.views.json_post'),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html')),
    url(r'^name$',    TemplateView.as_view(template_name='name.html')),
)
