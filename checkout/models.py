from django.db import models
from product_info.models import Items
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    streetName = models.CharField(max_length=255)
    streetNumber = models.CharField(max_length=255)
    zip = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    card_holder = models.CharField(max_length=255)
    card_number = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(16)])
    card_exp_month = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(2)])
    card_exp_year = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(2)])
    card_cvc = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(3)])


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase_History, on_delete=models.CASCADE)
    quantity = models.FloatField()
