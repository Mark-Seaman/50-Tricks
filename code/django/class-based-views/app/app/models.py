from django.db import models

# Create your models here.
class Contact(models.Model):
    name  = models.CharField (max_length=40)
    address  = models.CharField (max_length=100)    
    phone = models.CharField (max_length=15)
            
    class Meta:
        ordering = ["-name"]
        
    def __unicode__(self):
        return self.name
