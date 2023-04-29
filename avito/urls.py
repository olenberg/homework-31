from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads import views
from users.views import LocationViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register("locations", LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('categories/', include("categories.urls")),
    path('ads/', include("ads.urls")),
    path('users/', include("users.urls")),
    path('selections/', include("selections.urls")),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
