from django.db import models

# Create your models here.

class medicinedb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image= models.ImageField(upload_to="images",null=True,blank=True)

class empdata(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    salary = models.IntegerField(null=True,blank=True)
    image= models.ImageField(upload_to="images",null=True,blank=True)

