from django.db import models

# Create your models here.
class contact_us(models.Model):
     name = models.CharField(max_length=200)
     phone  = models.TextField()
     email = models.CharField(max_length=200) 
     text = models.CharField(max_length=500) 
     

     

      

              