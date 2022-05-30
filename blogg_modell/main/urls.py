from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name="search"),
    path('weather/', views.weatherAPI, name="weatherAPI"),
    path('add/', views.weatherSearch, name="weatherSearch"),
    path('api/', views.myAPI, name="myAPI"),
]
