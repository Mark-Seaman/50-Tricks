# views.py

# Direct HTML from view

# Template View -- class based view using a fixed template
# View from model -- class based view 
# Extra content in view
# Viewing subsets of objects
# Dynamic filtering
# Doing extra work
# Basic form editing
# Model forms
# Adding user info

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


from app.models import Contact


#-----------------------------------------------------------------------------
# List view

# Basic list view with using a template
class ContactList(ListView):
    model = Contact
    template_name = 'contact_list.html'



# Filter the rows with a query
class MyContactList(ListView):

    template_name = 'contact_list.html'
    #queryset = Contact.objects.filter(name__startswith='Contact ')

    def get_queryset(self):
        return Contact.objects.all()   #filter(user=self.request.user)


#-----------------------------------------------------------------------------
# Detail view

# Basic detail view
class ContactDetail(DetailView):
    model = Contact
    template_name = 'contact_detail.html'

# Specialized detail view
class MyContactDetail(DetailView):
    #context_object_name = 'contact'
    #queryset = Contact.objects.all()

    model = Contact
    template_name = 'contact_detail.html'

    # Call the base implementation first to get a context
    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        #context['name_list'] = [ 'Mark', 'Peter', 'Bob' ]
        return context

#-----------------------------------------------------------------------------
# Edit view

# Create view
class ContactCreate(CreateView):
    model = Contact
    fields = ['name','address', 'phone']
    template_name = 'contact_edit.html'

# Update view
class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name','address','phone']
    template_name = 'contact_edit.html'


#-----------------------------------------------------------------------------
# Edit view

# Delete view
class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
    template_name = 'contact_delete.html'


