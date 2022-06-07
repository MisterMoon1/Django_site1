"""Определяет схемы URL для learning_log2."""

from django.urls import path

from . import views

app_name = 'learning_log2'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index')
]