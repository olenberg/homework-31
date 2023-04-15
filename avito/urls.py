from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads import views as ads_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ads_views.index),
    path('categories/', ads_views.CategoryList.as_view()),
    path('categories/<int:pk>/', ads_views.CategoryDetail.as_view()),
    path('categories/<int:pk>/update/', ads_views.CategoryUpdate.as_view()),
    path('categories/create/', ads_views.CategoryCreate.as_view()),
    path('categories/<int:pk>/delete/', ads_views.CategoryDelete.as_view()),
    path('ads/', ads_views.AdList.as_view()),
    path('ads/<int:pk>/', ads_views.AdDetail.as_view()),
    path('ads/create/', ads_views.AdCreate.as_view()),
    path('ads/<int:pk>/delete/', ads_views.AdDelete.as_view()),
    path('ads/<int:pk>/update/', ads_views.AdUpdate.as_view()),
    path('ads/<int:pk>/upload_image/', ads_views.AdImage.as_view()),
    path('users/', users_views.UserList.as_view()),
    path('users/<int:pk>/', users_views.UserDetail.as_view()),
    path('users/<int:pk>/delete/', users_views.UserDelete.as_view()),
    path('users/create/', users_views.UserCreate.as_view()),
    path('users/<int:pk>/update/', users_views.UserUpdate.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
