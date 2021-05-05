from django.db import models
from account.models import User
from product_info.models import Items

# Create your models here.
class History(models.Model):
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE),
    item_ID = models.ForeignKey(Items, on_delete=models.CASCADE),
    time = models.FloatField()