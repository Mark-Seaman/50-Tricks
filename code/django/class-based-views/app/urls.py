# urls.py

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import TemplateView

from app.views import ContactList, ContactDetail, MyContactList
from app.views import ContactCreate, ContactUpdate, ContactDelete


urlpatterns = patterns('',  

    # Home view
    url(r'^$', TemplateView.as_view(template_name="contact.html")),
   
    # Detail view
    url(r'^contacts/(?P<pk>\d+)$', ContactDetail.as_view(), name='contact-detail'),

    # List view
    url(r'^contacts/$', ContactList.as_view(), name='contact_list'),
    url(r'^my-contacts/$', MyContactList.as_view()),

    # Add view
    url(r'contacts/add$', ContactCreate.as_view(), name='contact_add'),

    # Update view
    url(r'contacts/(?P<pk>\d+)/edit$', ContactUpdate.as_view(), name='contact_update'),

    # Delete view
    url(r'contacts/(?P<pk>\d+)/delete$', ContactDelete.as_view(), name='contact_delete'),
)
