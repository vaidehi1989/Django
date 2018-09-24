from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10)
    dob = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(default=0)

    def calAge(self):
        d = date.today()
        self.age = d.year - self.dob.year
        self.save()
