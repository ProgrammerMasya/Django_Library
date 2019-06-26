from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Book(models.Model):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'id': self.id})


class UserProfile(User):

    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.username
