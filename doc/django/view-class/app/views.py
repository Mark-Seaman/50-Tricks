# views.py
# Basic views

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from app.models import Contact


# Basic list view with using a template
class ContactList(ListView):
    model = Contact
    template_name = 'contact.html'

    # # Filter the list of choices
    # queryset = Contact.objects.filter(name__startswith='Contact ')

    # # Use the request user to match the items
    # def get_queryset(self):
    #     return Contact.objects.filter(name=self.request.user.username)


# Basic detail view
class ContactDetail(DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'

    # # Call the base implementation first to get a context
    # def get_context_data(self, **kwargs):
    #     context = super(MyContactDetail, self).get_context_data(**kwargs)
    #     context['name_list'] = [ 'Mark', 'Peter', 'Bob' ]
    #     return context


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


# Delete view
class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
    template_name = 'contact_delete.html'

