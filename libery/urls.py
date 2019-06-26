from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns

    def show_toolbar(request):
        return True
