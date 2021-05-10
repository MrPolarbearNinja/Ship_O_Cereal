from django.db import models
from product_info.models import Items
from django.contrib.auth.models import User

# Create your models here.
class Basket(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    item_ID = models.ForeignKey(Items, on_delete=models.CASCADE),
    quantity = models.FloatField()

