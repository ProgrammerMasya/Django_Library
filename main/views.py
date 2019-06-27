from .models import Book, UserProfile
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .forms import UserForm, BookCreateForm, UserEditForm
from django.core.paginator import Paginator
from django.db.models import Avg


class UserListView(TemplateView):

    template_name = 'home.html'
    model = UserProfile

    def get(self, request, *args, **kwargs):
        users = self.model.objects.all().annotate(Avg('book__price'))
        print(vars(users))
        paginator = Paginator(users, 5)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        args = {
            'users': page,
            'user_form': UserForm(),
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, request.FILES)
        users = self.model.objects.all().annotate(Avg('book__price'))
        paginator = Paginator(users, 5)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        if form.is_valid():
            form.save()
            form = UserForm()
        args = {
            'users': page,
            'user_form': form,
        }
        return render(request, self.template_name, args)

    def delete(self, id):
        user = UserProfile.objects.get(id=id)
        user.delete()
        return redirect('/')


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


class UserEditView(TemplateView):

    template_name = 'edit_user.html'

    def get(self, request, *args, **kwargs):
        try:
            user = UserProfile.objects.get(id=kwargs['id'])
        except:
            return Http404
        form = UserEditForm(instance=user)
        args = {
            'user_form': form,
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        try:
            user = UserProfile.objects.get(id=kwargs['id'])
        except:
            return Http404
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_list'))
        args = {
            'user_form': form
        }
        return render(request, self.template_name, args)