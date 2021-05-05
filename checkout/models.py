from django.db import models
from product_info.models import Items

# Create your models here.
class Address(models.Model):
    street_name = models.CharField(max_length=255),
    street_number = models.CharField(max_length=255),
    zip = models.FloatField()

class City(models.Model):
    name = models.CharField(max_length=255)

class Country(models.Model):
    name = models.CharField(max_length=255)

class Cards(models.Model):
    card_holder = models.CharField(max_length=255),
    card_number = models.FloatField(),
    expire_date = models.FloatField(),
    cvc = models.FloatField()

class Purchase_History(models.Model):
    fyrst_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    address_ID = models.ForeignKey(Address, on_delete=models.CASCADE),
    city_ID = models.ForeignKey(City, on_delete=models.CASCADE),
    country_ID = models.ForeignKey(Country, on_delete=models.CASCADE),
    card_ID = models.ForeignKey(Cards, on_delete=models.CASCADE)

class Checkout(models.Model):
    item_ID = models.ForeignKey(Items, on_delete=models.CASCADE),
    purchase_ID = models.ForeignKey(Purchase_History, on_delete=models.CASCADE),