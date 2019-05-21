from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    category = models.CharField(max_length=30)
    cover = models.FileField()

    def __str__(self):
        return self.category


class Item(models.Model):
    category = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    restaurant = models.CharField(max_length=25)
    location = models.CharField(max_length=30)



class Restaurant (models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name