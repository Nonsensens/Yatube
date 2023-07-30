from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('group/<int:pk>/', views.group_posts),
]
