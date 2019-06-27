from django import forms
from .models import Book, UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'password', 'image')
        help_texts = {
            'username': None,
        }

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if len(username) < 5:
            raise forms.ValidationError('Username не должен быть короче 5 символов')
        if len(password) < 8:
            raise forms.ValidationError('Password не должен быть короче 8 символов')
        if UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с данным логином уже зарегистрирован')


class UserEditForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name')
        help_texts = {
            'username': None,
        }


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author', 'price', 'pages_count', 'amazon_rating')

    def save(self, user):
        book = super(BookCreateForm, self).save(commit=False)
        book.user = user
        book.save()
        return book




