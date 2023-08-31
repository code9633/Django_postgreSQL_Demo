from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    
class Offer(models.Model):
    code = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    discount = models.FloatField()