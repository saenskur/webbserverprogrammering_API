#from django.contrib import admin
from django.urls import path
from django.urls.conf import include 
from . import views

urlpatterns = [
    path('', views.home, name="list"),
    path('add/', views.add, name="add"),
]
