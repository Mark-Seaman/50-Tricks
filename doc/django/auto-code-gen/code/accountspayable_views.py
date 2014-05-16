# views_dt.py
# AccountsPayable views

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from app.models import AccountsPayable


# Basic list view with using a template
class AccountsPayableList(ListView):
    model = AccountsPayable
    template_name = 'accountspayable_list.html'


# Basic detail view
class AccountsPayableDetail(DetailView):
    model = AccountsPayable
    template_name = 'accountspayable_detail.html'


# Create view
class AccountsPayableAdd(CreateView):
    model = AccountsPayable
    template_name = 'accountspayable_edit.html'


# Update view
@login_required(login_url='/login')
class AccountsPayableEdit(UpdateView):
    model = AccountsPayable
    template_name = 'accountspayable_edit.html'


# Delete view
class AccountsPayableDelete(DeleteView):
    model = AccountsPayable
    success_url = reverse_lazy('accountspayable_list')
    template_name = 'accountspayable_delete.html'
