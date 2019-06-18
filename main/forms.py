from django import forms
from django.contrib.auth.models import User
from .models import Book


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author')

    def save(self, user):
        book = super(BookCreateForm, self).save(commit=False)
        book.user = user
        book.save()
        return book
