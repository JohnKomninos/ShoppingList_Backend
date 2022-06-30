from django.db import models

# Create your models here.
class Sublist(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    aisle = models.IntegerField()
    quantity = models.IntegerField()
