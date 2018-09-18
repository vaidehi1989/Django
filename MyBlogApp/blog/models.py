from django.db import models
from django.utils import timezone

from django.urls import reverse


class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    # significance of str()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailview', args=[str(self.post.id)])


class Icecream(models.Model):
    name = models.CharField(max_length = 30)
    price = models.IntegerField()

    def __str__(self):
        return self.name
