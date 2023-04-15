from django.urls import path
from categories import views


urlpatterns = [
    path('', views.CategoryList.as_view()),
    path('<int:pk>/', views.CategoryDetail.as_view()),
    path('<int:pk>/update/', views.CategoryUpdate.as_view()),
    path('create/', views.CategoryCreate.as_view()),
    path('<int:pk>/delete/', views.CategoryDelete.as_view()),
]