from django import forms
from .models import Book, UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'password', 'image')


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author')

    def save(self, user):
        book = super(BookCreateForm, self).save(commit=False)
        book.user = user
        book.save()
        return book
