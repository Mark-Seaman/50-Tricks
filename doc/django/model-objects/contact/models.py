# models.py

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Contact(models.Model):
    name  = models.CharField (max_length=40)
    address  = models.CharField (max_length=100)    
    phone = models.CharField (max_length=15)
        
    def __unicode__(self):
        return self.name

    def __iter__(self):
        for i in self.fields():
            yield (i, getattr(self, i))
            
    def fields(self):
        return [ f.name for f in self._meta.fields ]

    def values(self):
        return [ v for f,v in self ]

    def table(self):
        return zip(self.fields(),self.values())


def print_contact(contact):
    for x in contact.table():
        print '    %-10s:  %s' % (x[0],x[1])


def show_contact(contact):
    print 'Contact:', contact.name
    print 'Fields:', contact.fields()
    print 'Values:', contact.values()
    print 'Table:', contact.table()
    print_contact(contact)


def add_fake_contact(name):
    c = Contact()
    c.name = name
    c.address = 'Here'
    c.phone = '900-555-1212'
    c.save()
    return c


def test_code():
    print 'Contact list:','There are ', len(Contact.objects.all()), 'objects'

    Contact.objects.all().delete()

    c = add_fake_contact('Billy')
    c = add_fake_contact('Bob')

    for c in Contact.objects.all():
        show_contact(c)

