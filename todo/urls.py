from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.addtask, name='addtask'),
    path('tasks/', views.tasks, name='tasks'),
]