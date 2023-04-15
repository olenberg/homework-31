from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('categories/', include("categories.urls")),
    path('ads/', include("ads.urls")),
    path('users/', include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
