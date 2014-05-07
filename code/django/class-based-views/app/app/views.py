from django.views.generic import ListView

from app.models import Contact

class ContactList(ListView):
    model = Contact
    template_name = 'contact_list.html'


# Work done:
# 1. Direct HTML from view
# 2. Template View -- class based view using a fixed template
# 3. View from model -- class based view 


# To implement:
# Extra content in view
# Viewing subsets of objects
# Dynamic filtering
# Doing extra work
# Basic form editing
# Model forms
# Adding user info
