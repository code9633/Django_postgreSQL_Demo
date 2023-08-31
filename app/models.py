from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    
    
class Ship(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.FloatField()
    no_of_items = models.IntegerField()
