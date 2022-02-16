from django.db import models
from django.forms import CharField
from django.db import models

# Create your models here.

class Owner(models.Model):
    name  = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age   = models.IntegerField(blank=True)
    #my_dog = models.ForeignObject('dog')
    class Meta:
        db_table = 'owners'
            
class Dog(models.Model):
    name  = models.CharField(max_length=45)
    owner = models.ForeignKey('Owner',on_delete=models.CASCADE)#relates_name="dogs")
    age   = models.IntegerField(blank=True)
    
    class Meta:
        db_table = 'dogs'
        

