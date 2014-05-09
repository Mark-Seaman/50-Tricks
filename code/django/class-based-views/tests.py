from app.models import Contact

def create_fake_contacts(id):
    print '%d Contacts found'% len(Contact.objects.all())
    c = Contact.objects.filter(pk=id)
    if len(c)==1:
        c = c[0]
        print 'Contact #%d already exists' % id
    else:
        c = Contact()
        print 'Contact #%d created' % id
    c.name = 'Contact #%d' % id
    c.address = 'Address #%d' % id
    c.phone = 'Phone #%d' % id
    c.save()

    
for c in range(10):
    create_fake_contacts(c+1)
