from django.db import models


class User(models.Model):

    name = models.CharField(max_length=100)


class Book(models.Model):

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
