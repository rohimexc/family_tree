from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField(null=True)
    no_hp= models.CharField(null=True,max_length=12)
    tgl_lahir=models.DateField(auto_now=False, auto_now_add=False)
    negara=models.CharField(null=True,max_length=200)
    kota=models.CharField(null=True,max_length=200)
    def __str__(self):
        return self.name