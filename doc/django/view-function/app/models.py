# models.py

from django.db import models
from django.core.urlresolvers import reverse
from django.forms       import ModelForm


# Create your models here.
class Contact(models.Model):
    name  = models.CharField (max_length=40)
    address  = models.CharField (max_length=100)    
    phone = models.CharField (max_length=15)

       
    class Meta:
        ordering = ["-name"]
        
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})


# Note form data model used to edit notes
class ContactForm (ModelForm):
    class Meta:
        model=Contact

