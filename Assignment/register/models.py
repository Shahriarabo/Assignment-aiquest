from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#  one to one relationship 
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=50)
    teacher_reg = models.IntegerField()
    
    
# many to one relationship 
class Coustomer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    coustomer_name = models.CharField(max_length=50)
    coustomer_address = models.CharField(max_length=50)
    coustomer_id = models.IntegerField()
    
    
    
    
# many to many relationship 
class Service(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    item = models.IntegerField()
  

    def service_man(self):
        return ",".join([str(p) for p in self.user.all()])
    
