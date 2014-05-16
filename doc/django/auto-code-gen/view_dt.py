# Views
from django.contrib.auth.decorators import login_required
from django.shortcuts   import render

from models   import Data_Type
from views    import list_page, show_page, add_page, delete_page, event_redirect
from views    import is_superuser, user

from data_type  import data_typees, data_type_get, data_type_detail, Data_TypeForm, data_type_fields
from data_type  import test_data_type

from util.log import log_page

# List
@login_required(login_url='/login')
def data_type_list(request):
    log_page (request, request.path)
    content =  {'title':'My Data_Typees', 'objects':data_typees(), 'otype':'data_type'}
    return list_page(request,content)

# Show
@login_required(login_url='/login')
def data_type_show(request,id):
    log_page (request, request.path)
    data_type = data_type_get(id)
    content = {'title':'Data_Type - '+data_type.name, 'fields':data_type_fields(data_type), 
               'otype':'data_type'}
    return show_page(request, content)

# Add
@login_required(login_url='/login')
def data_type_add(request):
    log_page (request, 'new')
    return add_page(request, data_type_form_data())
 
# Edit
@login_required(login_url='/login')
def data_type_edit(request,id=None):
    log_page (request, id)
    if request.method == 'POST':
        if request.POST.get('cancel', None):
            return event_redirect('/event/data_type/show/'+id)
        if id:
            data_type = data_type_get(id)
            form = Data_TypeForm(request.POST, instance=data_type)
            if form.is_valid():
                form.save()
                if id=='0':
                    return event_redirect('/event/data_type/list')
            return event_redirect('/event/data_type/show/'+id)
    return render(request, 'event_edit.html', data_type_form_data(id))

# Delete
@login_required(login_url='/login')
def data_type_delete(request,id):
    log_page (request, 'delete')
    item = data_type_get(id)
    link = '/event/data_type/list'
    content =  { 
        'title': 'Delete an Data_Type', 
        'item':  item, 
        'name':  item.name, 
        'index': link, 
        }
    return delete_page(request, content)
        
# Test
@login_required(login_url='/login')
def data_type_test(request):
    test_data_type()
    return data_type_list(request)


# Fill in the form
def data_type_form_data(id=None):
    if id:
        data_type = data_type_get(id)
        form = Data_TypeForm(instance=data_type)
        return  { 'form': form, 'id':data_type.id, 'title': 'Edit Data_Type', 'datatype':'data_type' }
    else:
        data_type  = Data_Type()
        form = Data_TypeForm()
        return  { 'form': form, 'id':'0', 'title': 'New Data_Type', 'datatype':'data_type' }

