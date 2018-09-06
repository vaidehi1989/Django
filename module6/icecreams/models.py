
from django.db import models

class Icecream(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
    	return self.name
