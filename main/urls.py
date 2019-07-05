from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
from .views import UserListView, BooksListView, BookEditView, UserEditView, BaseView

urlpatterns = [
    path('', BaseView.as_view(), name='user_list'),
    path('users/', UserListView.as_view(), name='user_list'),
    re_path('users/(?P<id>\d+)/$', BooksListView.as_view(), name='books_list'),
    re_path('book/(?P<id>\d+)/edit/$', BookEditView.as_view(), name='book_edit'),
    re_path('book/(?P<id>\d+)/del/$', UserListView.delete, name='delete_user'),
    re_path('user/(?P<id>\d+)/edit_user/$', UserEditView.as_view(), name='user_edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
