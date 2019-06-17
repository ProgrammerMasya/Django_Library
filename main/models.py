from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

    name = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
