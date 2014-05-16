from django.db          import models
from django.forms       import ModelForm
from django.shortcuts   import render_to_response, get_object_or_404
from django.db import models

from models import AccountsPayable


# Form for editing
class AccountsPayableForm(ModelForm):
    class Meta:
        model=AccountsPayable
        #fields = ('name', 'phone', 'email')    # Display only some fields


# Get a table listing from the database
def accountspayablees():
    return [ [ a.pk, a.name, a.phone ] for a in AccountsPayable.objects.all() ]


# Labels
accountspayable_labels = [ 'id', 'name', 'accountspayable1', 'accountspayable2', 'city', 'state', 'zipcode', 'phone', 
                   'tax_rate', 'email', 'notes',]

# Details
def accountspayable_detail(a):
    return [ a.pk, a.name, a.accountspayable1, a.accountspayable2, a.city, a.state, a.zipcode, a.phone, 
             a.tax_rate, a.email, a.notes,]


# Fields to show
def accountspayable_fields(a):
    return zip (accountspayable_labels,accountspayable_detail(a))


# Get an object or create it if needed
def accountspayable_get(id):
    a =  AccountsPayable.objects.filter(pk=id)
    if len(a)==1:
        return a[0]
    else:
        return AccountsPayable()


# Create an accountspayable record for testing
def create_accountspayable():
    a = AccountsPayable()
    a.save()
    a.name         = 'Name %d'%a.pk
    a.accountspayable1     = 'AccountsPayable %d'%a.pk
    a.city         = 'City %d'%a.pk
    a.state        = 'State %d'%a.pk
    a.zipcode      = 'Zip %d'%a.pk
    a.phone        = 'Phone %d'%a.pk
    a.email        = 'Email %d'%a.pk
    a.save()
    return a



#-----------------------------------------------------------------------------
# Test the database create and delete features

def test_accountspayable():
    #for a in AccountsPayable.objects.filter(name__startswith='Name ')all():
    #    a.delete()

    for a in range(10):
        create_accountspayable()

    #print accountspayable_list()



