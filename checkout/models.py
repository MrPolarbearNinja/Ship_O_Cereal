from django.db import models
from product_info.models import Items

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Purchase_History(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    streetName = models.CharField(max_length=255)
    streetNumber = models.CharField(max_length=255)
    zip = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Checkout(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase_History, on_delete=models.CASCADE)