import uuid
from django.db import models
from django.contrib.auth.models import User


class OptionCity(models.Model):
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.city

class OptionCountry(models.Model):
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.country


class Family(models.Model):
    jk=(('male','Laki-laki'),('female','Perempuan'))
    rl=(
        ('suami','suami'),
        ('istri','istri'),
        ('anak perempuan','anak perempuan'),
        ('anak laki-laki','anak laki-laki'),
        ('ayah','ayah'),
        ('ibu','ibu'),
        )
    name = models.CharField(max_length=200)
    email= models.EmailField(null=True,blank=True)
    phone= models.CharField(null=True,max_length=12, blank=True)
    gender= models.CharField(null=True,choices=jk, max_length=12)
    born=models.DateField(auto_now=False, auto_now_add=False,null=True)
    death=models.DateField(auto_now=False, auto_now_add=False,null=True)
    country=models.CharField(null=True,max_length=200, blank=True)
    city=models.CharField(null=True,max_length=200, blank=True)
    relation=models.CharField(null=True, choices=rl, max_length=200,blank=True)
    photo=models.ImageField(upload_to='profil',null=True)
    mid=models.IntegerField(null=True, blank=True)
    fid=models.IntegerField(null=True, blank=True)
    pids=models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    profil = models.CharField(max_length=100,null=True, blank=True)