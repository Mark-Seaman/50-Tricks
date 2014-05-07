from app.models import Contact

def create_fake_contacts(id):
    print '%d Contacts found'% len(Contact.objects.all())
    c = Contact.objects.filter(pk=id)
    if len(c)==1:
        print 'Contact #%d already exists' % id
    else:
        c = Contact()
        name = 'Contact #%d' % id
        address = 'Address #%d' % id
        phone = 'Phone #%d' % id
        c.save()
        print 'Contact #%d created' % id

    
for c in range(10):
    create_fake_contacts(c+1)
