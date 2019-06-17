from django import forms
from django.contrib.auth.models import User
from .models import Book


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


