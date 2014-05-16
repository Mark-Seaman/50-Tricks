# views_dt.py
# Data_Type views

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from app.models import Data_Type


# Basic list view with using a template
class Data_TypeList(ListView):
    model = Data_Type
    template_name = 'data_type_list.html'


# Basic detail view
class Data_TypeDetail(DetailView):
    model = Data_Type
    template_name = 'data_type_detail.html'


# Create view
class Data_TypeAdd(CreateView):
    model = Data_Type
    template_name = 'data_type_edit.html'


# Update view
@login_required(login_url='/login')
class Data_TypeEdit(UpdateView):
    model = Data_Type
    template_name = 'data_type_edit.html'


# Delete view
class Data_TypeDelete(DeleteView):
    model = Data_Type
    success_url = reverse_lazy('data_type_list')
    template_name = 'data_type_delete.html'
