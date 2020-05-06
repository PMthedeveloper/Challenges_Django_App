from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show', views.show, name='show'),
    path('Asc', views.Asc, name='Asc'),
    path('Dsc', views.Dsc, name='Dsc'),
]
