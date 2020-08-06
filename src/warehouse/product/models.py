from django.db import models


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=55)
    name = models.CharField(max_length=100)
    value = models.FloatField()
    discount = models.FloatField()
    stock = models.IntegerField()
