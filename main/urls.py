from django.contrib import admin
from django.urls import path, re_path
from .views import UserListView, BooksListView, BookEditView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    re_path('(?P<id>\d+)/$', BooksListView.as_view(), name='books_list'),
    re_path('(?P<id>\d+)/edit/$', BookEditView.as_view(), name='book_edit'),
]
