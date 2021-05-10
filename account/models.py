from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, blank=True)




