# urls_dt.py
# Data_Type urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',

    # Data_Type  (List, Detail, Add, Edit, Delete, Test)
    url(r'^data_type/$',                      'view_data_type.Data_TypeList'),
    url(r'^data_type/(?P<id>[\d]+)$',         'view_data_type.Data_TypeDetail'),
    url(r'^data_type/add$',                   'view_data_type.Data_TypeAdd'),
    url(r'^data_type/(?P<id>[\d]+)/edit$',    'view_data_type.Data_TypeEdit'),
    url(r'^data_type/(?P<id>[\d]+)/delete$',  'view_data_type.Data_TypeDelete'),
    url(r'^data_type/test$', TemplateView.as_view(template_name="data_type_test.html")),

    # Catch all view
    url(r'^(?P<title>[\w\-_./]+)$',   'event.views.missing_view'),

)
