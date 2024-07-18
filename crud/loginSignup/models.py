from django.db import models

# Create your models here.
class userdata(models.Model):
    username = models.CharField(max_length = 10,unique = True)
    password1 = models.CharField(max_length = 10)
    password2 = models.CharField(max_length = 10)
    image = models.ImageField(max_length=200)
        