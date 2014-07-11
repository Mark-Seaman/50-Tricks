# views.py
# Basic views

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template    import loader, RequestContext, Context
from django.shortcuts   import render_to_response
from django.http        import HttpResponseRedirect, HttpResponse

from app.models import Contact,ContactForm


# Render the appropriate doc view
def contact_list (request):
    page = loader.get_template ('contact.html')
    context = Context({ 'object_list': Contact.objects.all() })
    return HttpResponse(page.render(context))


# Get the object or create a new one
def lookup(pk):
    if pk != '0':
        return Contact.objects.get(pk=pk)
    else:
        return Contact()


# Render the add view
def contact_edit(request,pk='0'):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            c = lookup(pk)
            c.name = form.data['name']
            c.address = form.data['address']
            c.phone = form.data['phone']
            c.save()
            return HttpResponseRedirect('/')
    else: 
        c = lookup(pk)
    data =  { 'form': ContactForm (instance=c) }
    template = 'contact_edit.html'
    return render_to_response(template, data, context_instance=RequestContext(request))


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


# Delete view
class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
    template_name = 'contact_delete.html'

