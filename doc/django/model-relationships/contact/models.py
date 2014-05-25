# models.py
# Demonstrate many to many relationships

from django.db import models


class Contact(models.Model):
    name  = models.CharField (max_length=40)
    address  = models.CharField (max_length=100)    
    phone = models.CharField (max_length=15)
        
    def __unicode__(self):
        return self.name

    # Data field handling
    def __iter__(self):
        for i in self.fields():
            yield (i, getattr(self, i))
            
    def fields(self):
        return [ f.name for f in self._meta.fields ]

    def values(self):
        return [ v for f,v in self ]

    def table(self):
        return zip(self.fields(),self.values())


class Company(models.Model):
    name  = models.CharField (max_length=40)
    address  = models.CharField (max_length=100)    
    contacts = models.ManyToManyField (Contact)

    def __unicode__(self):
        return self.name

    # Data field handling
    def __iter__(self):
        for i in self.fields():
            yield (i, getattr(self, i))
            
    def fields(self):
        return [ f.name for f in self._meta.fields ]

    def values(self):
        return [ v for f,v in self ]

    def table(self):
        return zip(self.fields(),self.values())


#-----------------------------------------------------------------------------
# Usage of models

def clear():
    Contact.objects.all().delete()
    Company.objects.all().delete()


def print_contact(contact):
    for x in contact.table():
        print '    %-10s:  %s' % (x[0],x[1])
    if len(contact.company_set.all())>0:
        print '    %-10s: '%'companies',
        print ', '.join([ c.name for c in contact.company_set.all() ])
    print


def print_company(company):
    for x in company.table():
        print '    %-10s:  %s' % (x[0],x[1])
    if len(company.contacts.all())>0:
        print '    %-10s: '%'contacts',
        print ', '.join([ c.name for c in company.contacts.all() ])
    print


def print_all_companies():
    contacts = Contact.objects.all()
    print ('-' * 77)
    print "Contacts:  %d records found"%len(contacts)
    for c in contacts:
        print_contact(c)


def print__all_contacts():
    companies = Company.objects.all()
    print ('-' * 77)
    print 'Companies:  %d records found'%len(companies)
    for c in companies:
        print_company(c)


def get_contact(name):
    contacts = Contact.objects.filter(name=name)
    if len(contacts)<1:
        return Contact()
    else:
        return contacts[0]


def get_company(name):
    c = Company.objects.filter(name=name)
    if len(c)<1:
        return Company()
    else:
        return c[0]  


def add_fake_contact(name):
    c = get_contact(name)
    c.name = name
    c.address = 'Here'
    c.phone = '900-555-1212'
    c.save()
    return c


def add_fake_company(name):
    c = get_company(name)
    c.name = name
    c.address = 'There you are'
    c.phone = '303-555-1212'
    c.save()
    return c


def assign(contact,company):
    add_fake_contact(contact)
    add_fake_company(company)
    get_company(company).contacts.add(get_contact(contact))


def test_code():
    #clear()

    assign('Don',    'Impact Group')
    assign('Brad',   'Impact Group')
    assign('Eric',   'Impact Group')
    assign('Mark',   'Impact Group')
    assign('Ron',    'App Thumper')
    assign('Steph',  'App Thumper')
    assign('Mark',   'App Thumper')
    assign('Mark',   'Shrinking World Solutions')
    assign('Eric',   'Shrinking World Solutions')

    print_all_companies()
    print__all_contacts()
 
