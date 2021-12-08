from django.contrib import admin
from django.urls import path
#Person 3, här behövs importeras views från denna mapp

urlpatterns = [
    #((Person 2) här behövs läggas till en koppling till view-funktionen register)
    path('',  , name="register"),

]