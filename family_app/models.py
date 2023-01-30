from django.db import models
from django.contrib.auth.models import User

# Create your models here. =
class OptionFamily(models.Model):
    idf = models.IntegerField(null=True)
    name = models.CharField(max_length=50,null=True)
    mid=models.IntegerField(null=True, blank=True)
    fid=models.IntegerField(null=True, blank=True)
    pids=models.IntegerField(null=True)

    def __str__(self):
        return self.name

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
    email= models.EmailField(null=True)
    phone= models.CharField(null=True,max_length=12)
    gender= models.CharField(null=True,choices=jk, max_length=12)
    born=models.DateField(auto_now=False, auto_now_add=False)
    country=models.CharField(null=True,max_length=200)
    city=models.CharField(null=True,max_length=200)
    relation=models.CharField(null=True, choices=rl, max_length=200)
    relation_from=models.ForeignKey(OptionFamily, on_delete=models.CASCADE, null=True)
    mid=models.IntegerField(null=True, blank=True)
    fid=models.IntegerField(null=True, blank=True)
    pids=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name