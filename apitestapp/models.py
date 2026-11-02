from turtle import title

from django.db import models
from django.utils.http import MAX_URL_LENGTH

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
