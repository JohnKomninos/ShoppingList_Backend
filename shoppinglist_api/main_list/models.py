from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    aisle = models.IntegerField()
    listname = models.CharField(max_length=32, default="")
