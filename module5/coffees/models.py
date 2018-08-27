
from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    rosat_level = models.CharField(max_length=30)
    price = models.IntegerField()
    processing_type = models.CharField(max_length=30)

    def __str__(self):
    	return self.name
