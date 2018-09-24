from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # when form is submitted it takes you to mentioned url
    # Only for class-based views.
    def get_absolute_url(self):
        return reverse('detailview', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=140)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        return reverse('detailview', args=[str(self.post.id)])
