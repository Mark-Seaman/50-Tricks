from django.db          import models
from django.forms       import ModelForm
from django.shortcuts   import render_to_response, get_object_or_404
from django.db import models

from models import EventMenu


# Form for editing
class EventMenuForm(ModelForm):
    class Meta:
        model=EventMenu
        #fields = ('name', 'phone', 'email')    # Display only some fields


# Get a table listing from the database
def eventmenues():
    return [ [ a.pk, a.name, a.phone ] for a in EventMenu.objects.all() ]


# Labels
eventmenu_labels = [ 'id', 'name', 'eventmenu1', 'eventmenu2', 'city', 'state', 'zipcode', 'phone', 
                   'tax_rate', 'email', 'notes',]

# Details
def eventmenu_detail(a):
    return [ a.pk, a.name, a.eventmenu1, a.eventmenu2, a.city, a.state, a.zipcode, a.phone, 
             a.tax_rate, a.email, a.notes,]


# Fields to show
def eventmenu_fields(a):
    return zip (eventmenu_labels,eventmenu_detail(a))


# Get an object or create it if needed
def eventmenu_get(id):
    a =  EventMenu.objects.filter(pk=id)
    if len(a)==1:
        return a[0]
    else:
        return EventMenu()


# Create an eventmenu record for testing
def create_eventmenu():
    a = EventMenu()
    a.save()
    a.name         = 'Name %d'%a.pk
    a.eventmenu1     = 'EventMenu %d'%a.pk
    a.city         = 'City %d'%a.pk
    a.state        = 'State %d'%a.pk
    a.zipcode      = 'Zip %d'%a.pk
    a.phone        = 'Phone %d'%a.pk
    a.email        = 'Email %d'%a.pk
    a.save()
    return a



#-----------------------------------------------------------------------------
# Test the database create and delete features

def test_eventmenu():
    #for a in EventMenu.objects.filter(name__startswith='Name ')all():
    #    a.delete()

    for a in range(10):
        create_eventmenu()

    #print eventmenu_list()



