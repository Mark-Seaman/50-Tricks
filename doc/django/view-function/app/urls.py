# urls.py

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from app.views   import ContactList, ContactDetail, ContactCreate, ContactUpdate, ContactDelete


urlpatterns = patterns('',  

    # List view
    #url(r'^$',                           ContactList.as_view(), name='contact_list'),
    url(r'^$',                           'app.views.contact_list', name='contact_list'),

    # Detail view
    url(r'^contacts/(?P<pk>\d+)$',       ContactDetail.as_view(), name='contact-detail'),

    # Add view
   #url(r'contacts/add$',                ContactCreate.as_view(), name='contact_add'),
    url(r'contacts/add$',               'app.views.contact_edit'),

    # Update view
    #url(r'contacts/(?P<pk>\d+)/edit$',   ContactUpdate.as_view(), name='contact_update'),
    url(r'contacts/(?P<pk>\d+)/edit$',    'app.views.contact_edit', name='contact_update'),

    # Delete view
    url(r'contacts/(?P<pk>\d+)/delete$', ContactDelete.as_view(), name='contact_delete'),

)
