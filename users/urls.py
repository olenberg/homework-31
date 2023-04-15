from django.urls import path
from users import views


urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('<int:pk>/delete/', views.UserDelete.as_view()),
    path('create/', views.UserCreate.as_view()),
    path('<int:pk>/update/', views.UserUpdate.as_view())
]