from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    ingredients = models.CharField(max_length=30, null=False, blank=False)
    price = models.IntegerField(null=False,blank=False)