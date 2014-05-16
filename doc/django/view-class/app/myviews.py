# views.py
# Advanced views

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from app.models import Contact


# Filter the rows with a query
class MyContactList(ListView):

    template_name = 'contact_list.html'

    # Filter the list of choices
    queryset = Contact.objects.filter(name__startswith='Contact ')

    # Use the request user to match the items
    def get_queryset(self):
        return Contact.objects.filter(name=self.request.user.username)


# Specialized detail view
class MyContactDetail(DetailView):
    model = Contact
    template_name = 'contact_detail.html'

    # Choose the name used by the template
    context_object_name = 'contact'

    # Call the base implementation first to get a context
    def get_context_data(self, **kwargs):
        context = super(MyContactDetail, self).get_context_data(**kwargs)
        context['name_list'] = [ 'Mark', 'Peter', 'Bob' ]
        return context


# Create view
class MyContactCreate(CreateView):
    model = Contact
    fields = ['name','address', 'phone']
    template_name = 'contact_edit.html'


# Update view
class MyContactUpdate(UpdateView):
    model = Contact
    fields = ['name','address','phone']
    template_name = 'contact_edit.html'


