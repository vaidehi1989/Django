
from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    flavour = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    price = models.IntegerField()
    processing = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
    	return self.name
