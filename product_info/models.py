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
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.FloatField()

class Items_Image(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    image_link = models.CharField(max_length=255)

    def __str__(self):
        return str(self.image_link)

