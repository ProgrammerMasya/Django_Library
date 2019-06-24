from .models import Book, UserProfile
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .forms import UserForm, BookCreateForm


class UserListView(TemplateView):

    template_name = 'home.html'
    model = UserProfile

    def get(self, request, *args, **kwargs):
        args = {
            'users': self.model.objects.all(),
            'user_form': UserForm(),
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
        args = {
            'users': self.model.objects.all(),
            'user_form': form,
        }
        return render(request, self.template_name, args)


class BooksListView(TemplateView):

    template_name = 'books.html'

    def get(self, request, *args, **kwargs):
        try:
            user = UserProfile.objects.get(id=kwargs['id'])
        except:
            return Http404
        args = {
            'user': user,
            'books': Book.objects.filter(user=user),
            'book_form': BookCreateForm(),
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        try:
            user = UserProfile.objects.get(id=kwargs['id'])
        except:
            return Http404
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save(user)
            form = BookCreateForm()
        args = {
            'user': user,
            'books': Book.objects.filter(user=user),
            'book_form': form,
        }
        return render(request, self.template_name, args)


class BookEditView(TemplateView):

    template_name = 'edit.html'

    def get(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(id=kwargs['id'])
        except:
            return Http404
        form = BookCreateForm(instance=book)
        args = {
            'book_form': form,
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(id=kwargs['id'])
        except:
            return Http404
        form = BookCreateForm(request.POST, instance=book)
        if form.is_valid():
            form.save(book.user)
            return redirect(reverse('books_list', kwargs={'id': book.user_id}))
        args = {
            'book_form': form
        }
        return render(request, self.template_name, args)