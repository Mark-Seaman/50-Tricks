# urls_dt.py
# AccountsPayable urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',

    # AccountsPayable  (List, Detail, Add, Edit, Delete, Test)
    url(r'^accountspayable/$',                      'view_accountspayable.AccountsPayableList'),
    url(r'^accountspayable/(?P<id>[\d]+)$',         'view_accountspayable.AccountsPayableDetail'),
    url(r'^accountspayable/add$',                   'view_accountspayable.AccountsPayableAdd'),
    url(r'^accountspayable/(?P<id>[\d]+)/edit$',    'view_accountspayable.AccountsPayableEdit'),
    url(r'^accountspayable/(?P<id>[\d]+)/delete$',  'view_accountspayable.AccountsPayableDelete'),
    url(r'^accountspayable/test$', TemplateView.as_view(template_name="accountspayable_test.html")),

    # Catch all view
    url(r'^(?P<title>[\w\-_./]+)$',   'event.views.missing_view'),

)
