# Views
from django.contrib.auth.decorators import login_required
from django.shortcuts   import render

from models   import EventMenu
from views    import list_page, show_page, add_page, delete_page, event_redirect
from views    import is_superuser, user

from eventmenu  import eventmenues, eventmenu_get, eventmenu_detail, EventMenuForm, eventmenu_fields
from eventmenu  import test_eventmenu

from util.log import log_page

# List
@login_required(login_url='/login')
def eventmenu_list(request):
    log_page (request, request.path)
    content =  {'title':'My EventMenues', 'objects':eventmenues(), 'otype':'eventmenu'}
    return list_page(request,content)

# Show
@login_required(login_url='/login')
def eventmenu_show(request,id):
    log_page (request, request.path)
    eventmenu = eventmenu_get(id)
    content = {'title':'EventMenu - '+eventmenu.name, 'fields':eventmenu_fields(eventmenu), 
               'otype':'eventmenu'}
    return show_page(request, content)

# Add
@login_required(login_url='/login')
def eventmenu_add(request):
    log_page (request, 'new')
    return add_page(request, eventmenu_form_data())
 
# Edit
@login_required(login_url='/login')
def eventmenu_edit(request,id=None):
    log_page (request, id)
    if request.method == 'POST':
        if request.POST.get('cancel', None):
            return event_redirect('/event/eventmenu/show/'+id)
        if id:
            eventmenu = eventmenu_get(id)
            form = EventMenuForm(request.POST, instance=eventmenu)
            if form.is_valid():
                form.save()
                if id=='0':
                    return event_redirect('/event/eventmenu/list')
            return event_redirect('/event/eventmenu/show/'+id)
    return render(request, 'event_edit.html', eventmenu_form_data(id))

# Delete
@login_required(login_url='/login')
def eventmenu_delete(request,id):
    log_page (request, 'delete')
    item = eventmenu_get(id)
    link = '/event/eventmenu/list'
    content =  { 
        'title': 'Delete an EventMenu', 
        'item':  item, 
        'name':  item.name, 
        'index': link, 
        }
    return delete_page(request, content)
        
# Test
@login_required(login_url='/login')
def eventmenu_test(request):
    test_eventmenu()
    return eventmenu_list(request)


# Fill in the form
def eventmenu_form_data(id=None):
    if id:
        eventmenu = eventmenu_get(id)
        form = EventMenuForm(instance=eventmenu)
        return  { 'form': form, 'id':eventmenu.id, 'title': 'Edit EventMenu', 'datatype':'eventmenu' }
    else:
        eventmenu  = EventMenu()
        form = EventMenuForm()
        return  { 'form': form, 'id':'0', 'title': 'New EventMenu', 'datatype':'eventmenu' }

