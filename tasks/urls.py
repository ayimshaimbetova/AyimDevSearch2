
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),
    path('my-login/', views.my_login),
    path('', views.home),
    path('view-tasks/', views.viewTasks, name='view-task'),
    path('create-task/', views.createTask),
]