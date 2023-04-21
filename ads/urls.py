from django.urls import path
from ads import views


urlpatterns = [
    path('', views.AdListView.as_view()),
    path('<int:pk>/', views.AdDetail.as_view()),
    path('create/', views.AdCreate.as_view()),
    path('<int:pk>/delete/', views.AdDelete.as_view()),
    path('<int:pk>/update/', views.AdUpdate.as_view()),
    path('<int:pk>/upload_image/', views.AdImage.as_view()),
]