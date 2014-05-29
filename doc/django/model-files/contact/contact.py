# models.py
# Demonstrate many to many relationships

from django.db import models


class Contact(models.Model):
    name  = models.CharField (max_length=40)
    address  = models.CharField (max_length=100)    
    phone = models.CharField (max_length=15)
        
    def __unicode__(self):
        return self.name

    # Data field handling
    def __iter__(self):
        for i in self.fields():
            yield (i, getattr(self, i))
            
    def fields(self):
        return [ f.name for f in self._meta.fields ]

    def values(self):
        return [ v for f,v in self ]

    def table(self):
        return zip(self.fields(),self.values())
