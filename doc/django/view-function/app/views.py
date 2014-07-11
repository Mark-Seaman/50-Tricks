# views.py
# Basic views

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template    import loader, RequestContext, Context
from django.shortcuts   import render_to_response
from django.http        import HttpResponseRedirect, HttpResponse

from app.models import Contact,ContactForm


# Render a form for editing
def form_render(request,template,data):
    return render_to_response(template, data, context_instance=RequestContext(request))


# Render a web page
def render(request,template,data): 
    page = loader.get_template (template)
    return HttpResponse(page.render(Context(data)))


# Render the appropriate doc view
def contact_list (request):
    content =  { 'object_list':Contact.objects.all() }
    return render(request, 'contact.html', content)


# Go to a specific page
def redirect(request,page):
    return ('/'+title) 


# Render the add view
def contact_edit(request,pk='0'):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if pk != '0':
                c = Contact.objects.get(pk=pk)
            else:
                c = Contact()
            c.name = form.data['name']
            c.address = form.data['address']
            c.phone = form.data['phone']
            c.save()
            return HttpResponseRedirect('/')
    else: 
        if pk != '0': 
            c = Contact.objects.get(pk=pk)
        else:
            c = Contact()

    data =  { 'form': ContactForm (instance=c) }
    return form_render (request, 'contact_edit.html', data)


#-----------------------------------------------------------------------------

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

