from django.db import models

# Create your models here.
class Item_Type(models.Model):
    name = models.CharField(max_length=255)

class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.FloatField()
    type = models.ForeignKey(Item_Type, on_delete=models.CASCADE)

class Item_Stock(models.Model):
    item = models.ForeignKey(Item_Type, on_delete=models.CASCADE)
    quantity = models.FloatField()

class Items_Image(models.Model):
    item = models.ForeignKey(Item_Type, on_delete=models.CASCADE)
    item_link = models.CharField(max_length=255)

