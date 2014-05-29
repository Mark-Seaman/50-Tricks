# urls.py

# Django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# App imports
from app.views   import ContactList, ContactDetail, ContactCreate, ContactUpdate, ContactDelete
from app.myviews import MyContactDetail, MyContactList, MyContactCreate, MyContactUpdate 
from app.myviews import ProtectedView


urlpatterns = patterns('',  

    # Home view
    url(r'^$', ProtectedView.as_view()),

    # From impact project
    #url(r'^$', 'views.home'),
    #url(r'^secure$', 'views.secure'),
    #url(r'^no_access$', 'views.no_access'),

    (r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),  
    #(r'^logout', 'views.logout_view'),

   
    # Detail view
    url(r'^contacts/(?P<pk>\d+)$',       ContactDetail.as_view(), name='contact-detail'),

    # List view
    url(r'^contacts/$',                  ContactList.as_view(), name='contact_list'),

    # Add view
    url(r'contacts/add$',                login_required(ContactCreate.as_view()), name='contact_add'),

    # Update view
    url(r'contacts/(?P<pk>\d+)/edit$',   login_required(ContactUpdate.as_view()), name='contact_update'),

    # Delete view
    url(r'contacts/(?P<pk>\d+)/delete$', login_required(ContactDelete.as_view()), name='contact_delete'),


    # Specialized views
    url(r'^my-contacts/(?P<pk>\d+)$',      MyContactDetail.as_view()),
    url(r'^my-contacts/$',                 MyContactList.as_view()),
    url(r'^my-contacts/add$',              MyContactCreate.as_view()),
    url(r'^my-contacts/(?P<pk>\d+)/edit$', MyContactUpdate.as_view()),
)



