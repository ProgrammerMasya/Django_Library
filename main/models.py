from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class Book(models.Model):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0000.00)
    pages_count = models.IntegerField(default=0)
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        if self.created_add:
            self.updated_add = datetime.now()
        super(Book, self).save(*args, **kwargs)


class UserProfile(User):

    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.username
