from django.db          import models
from django.forms       import ModelForm
from django.shortcuts   import render_to_response, get_object_or_404
from django.db import models

from models import Data_Type


# Form for editing
class Data_TypeForm(ModelForm):
    class Meta:
        model=Data_Type
        #fields = ('name', 'phone', 'email')    # Display only some fields


# Get a table listing from the database
def data_typees():
    return [ [ a.pk, a.name, a.phone ] for a in Data_Type.objects.all() ]


# Labels
data_type_labels = [ 'id', 'name', 'data_type1', 'data_type2', 'city', 'state', 'zipcode', 'phone', 
                   'tax_rate', 'email', 'notes',]

# Details
def data_type_detail(a):
    return [ a.pk, a.name, a.data_type1, a.data_type2, a.city, a.state, a.zipcode, a.phone, 
             a.tax_rate, a.email, a.notes,]


# Fields to show
def data_type_fields(a):
    return zip (data_type_labels,data_type_detail(a))


# Get an object or create it if needed
def data_type_get(id):
    a =  Data_Type.objects.filter(pk=id)
    if len(a)==1:
        return a[0]
    else:
        return Data_Type()


# Create an data_type record for testing
def create_data_type():
    a = Data_Type()
    a.save()
    a.name         = 'Name %d'%a.pk
    a.data_type1     = 'Data_Type %d'%a.pk
    a.city         = 'City %d'%a.pk
    a.state        = 'State %d'%a.pk
    a.zipcode      = 'Zip %d'%a.pk
    a.phone        = 'Phone %d'%a.pk
    a.email        = 'Email %d'%a.pk
    a.save()
    return a



#-----------------------------------------------------------------------------
# Test the database create and delete features

def test_data_type():
    #for a in Data_Type.objects.filter(name__startswith='Name ')all():
    #    a.delete()

    for a in range(10):
        create_data_type()

    #print data_type_list()



