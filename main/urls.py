from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('user', admin.site.urls),
]
