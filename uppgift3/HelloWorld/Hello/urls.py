#from django.contrib import admin
from django.urls import path
from django.urls.conf import include 
from . import views

urlpatterns = [
    path('', views.Extra, name="Extra"),
    path('home/' , views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('forms/', views.Forms, name='Forms'),
    path('home/<str:name>', views.greet, name='greet'),
]
