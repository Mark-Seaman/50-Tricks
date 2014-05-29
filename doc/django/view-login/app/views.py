# views.py
# Basic views

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from app.models import Contact


# Basic list view with using a template
class ContactList(ListView):
    model = Contact
    template_name = 'contact_list.html'


# Basic detail view
class ContactDetail(DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'


# Create view
class ContactCreate(CreateView):
    model = Contact
    template_name = 'contact_edit.html'


# Update view
class ContactUpdate(UpdateView):
    model = Contact
    template_name = 'contact_edit.html'


# Delete view
class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
    template_name = 'contact_delete.html'

