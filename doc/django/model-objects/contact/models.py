# models.py

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Contact(models.Model):
    name  = models.CharField (max_length=40)
    address  = models.CharField (max_length=100)    
    phone = models.CharField (max_length=15)

       
    class Meta:
        ordering = ["-name"]
        
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

    def __iter__(self):
        for i in self._meta.get_all_field_names():
            yield (i, getattr(self, i))
            

def fields(contact):
    return contact.__dict__


def show_fields(contact):

    print 'Contact:',contact.name
    
    for field, val in contact:
        print '    ',field, val
    #dir(contact._meta.)
        

def list_contact_model_fields():
    print Contact._meta.get_all_field_names()
    print Contact._meta.fields
    

def add_fake_contact():
    c = Contact()
    c.name = 'Me'
    c.address = 'Here'
    c.phone = '900-555-1212'
    c.save()


def list_contacts():
    print 'Contact list:'
    print 'There are ', len(Contact.objects.all()), 'objects'
    for x in Contact.objects.all()[:1]:
        show_fields(x)


def test_contact_code():
    list_contacts()
    list_contact_model_fields()
