from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save

# Create your models here.
class EmployeeData(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30,unique = True)
    department = models.CharField(max_length = 30)
    contact = models.IntegerField()
    address = models.CharField(max_length = 10)
    image = models.ImageField(upload_to='images/',blank=True)
    
def save_post(sender, instance, **kwargs):
    print("post save working")

post_save.connect(save_post, sender=EmployeeData) 

def save_pre(sender, instance, **kwargs):
    print("pre save working")
    
pre_save.connect(save_pre,sender=EmployeeData)   
    
    
    
# class student(models.Model):
#     name = models.CharField(max_length=10)
#     class meta:
#         abstract = True
#         proxy = True        

        
# class studentchild(student):
#     city = models.CharField(max_length=20)        
    
 
        
        