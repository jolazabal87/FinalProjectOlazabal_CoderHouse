from unicodedata import name
from django.db import models

# Create your models here.

class Brands(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    #logo = models.ImageField(upload_to='images/', null=True, blank=True)

class Categories(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
       
class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    bar_code = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField() 
    #img = models.ImageField(upload_to='images/', null=True, blank=True)
    active = models.BooleanField()
    
    def __str__(self):
        return f"Producto: {self.name}"

class Clients(models.Model):
    name = models.CharField(max_length=20)
    tax_code = models.IntegerField()
    address = models.CharField(max_length=20)
    cluster = models.CharField(max_length=20)
    contact = models.EmailField()
    #web_site = models.URLField()
    #logo = models.ImageField(upload_to='images/', null=True, blank=True)
    active = models.BooleanField()

class Suppliers(models.Model):
    name = models.CharField(max_length=20)
    tax_code = models.IntegerField()
    cluster = models.CharField(max_length=20)
    contact = models.EmailField()
    #web_site = models.URLField()
    #logo = models.ImageField(upload_to='images/', null=True, blank=True)
    active = models.BooleanField()

class Purchase_order(models.Model):
    date = models.DateField()
    client = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()
    delivery_address = models.CharField(max_length=20)
    delivery_date = models.DateField()
    active = models.BooleanField()
    