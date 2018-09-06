
from django.db import models

class Icecream(models.Model):
    
    name = models.CharField(max_length=30)

    category = models.CharField(max_length=30)

    price = models.IntegerField()


# Significance of str() - string representation of object
    def __str__(self):
    	return "{}  {}  {}".format(self.name,self.category,self.price)

