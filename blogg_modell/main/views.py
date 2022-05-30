from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Post
from django.template import loader
from django.urls import reverse
from django.views import generic
from django import forms
from django.forms.forms import Form
import requests
from .forms import RegisterForm, NewTaskForm
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#views go here

#Home/Index
def index(request):
    post = Post.objects.all()
    return render(request, "blogg/index.html", {'queryset':post})

#Register account
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/blogg")
    else: 
        form = RegisterForm()

    return render(response, 'registration/register.html', {"form":form})


#Search bar
def search(request):
    if request.method=="POST":
        author = request.POST['search']
        print(author)
        try:
            searched_author = Author.objects.get(name=author)
            posts_by_author = Post.objects.filter(author=searched_author)
        except:
            searchResponse = "Your request didn't match anything in our database"
            return render(request, "blogg/search.html", {'response':searchResponse,})
        else:
            return render(request, "blogg/search.html", {'queryset':posts_by_author})
    else:
        return render(request, "blogg/search.html")


#Pokemon API
def myAPI(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')
    context = response.json()
    types = [context['types'][0]['type']['name']]
    if context['types'][1]['type']['name']:
        types.append(context['types'][1]['type']['name'])
    return render(request, 'blogg/myapi.html', {
        'pokemon_name': context['name'],
        'pokemon_type': types})




#Weather API

apiList={}

def weatherSearch(request):
    key = "4f14ec29516d493785470208222904"
    tasklist=[]
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            city=form.cleaned_data["city"]
            days=form.cleaned_data["days"]
            tasklist.append(city)
            tasklist.append(days)
            response = requests.get('http://api.weatherapi.com/v1/forecast.json?key='+key+'&q='+city+'&days='+str(days)+'&aqi=no&alerts=no')
            context = response.json()
            if context:
                for stuff in context["current"]:
                    if stuff == "condition":
                        for condiment in context["current"]["condition"]:
                            tasklist.append(condiment)
                    else:
                        tasklist.append(stuff)
                for stuff2 in context["current"]:
                    tasklist.append(stuff2)

                #dictionary to be used in weather.html with template python
                apiList = {
                'icon': [context['current']['condition']['icon']],
                'name': context["location"]["name"],
                'temp_c': [context["current"]["temp_c"]],
                'text': [context['current']['condition']['text']],
                'date': [context['current']['last_updated']],
                }
                #iterate and add object to dictionary value lists
                for i in range(1, days):
                    apiList['icon'].append(context['forecast']['forecastday'][i]['day']['condition']['icon'])
                    apiList['temp_c'].append(context['forecast']['forecastday'][i]['day']['avgtemp_c'])
                    apiList['text'].append(context['forecast']['forecastday'][i]['day']['condition']['text'])
                    apiList['date'].append(context['forecast']['forecastday'][i]['date'])
                
            return render(request, 'blogg/weather.html', {
                'tasklist':tasklist,
                'form':form,
                "mydict":apiList,
                'range': range(days),
                'request': city,
            })
        else:
            return redirect('http://127.0.0.1:8000/blogg/')
    return render(request, 'blogg/weather.html', {
        "form":NewTaskForm()
    })


def weatherAPI(request):
    key = "4f14ec29516d493785470208222904"
    city = "Stockholm"
    days = 1
    response = requests.get('http://api.weatherapi.com/v1/forecast.json?key='+key+'&q='+city+'&days='+str(days)+'&aqi=no&alerts=no')
    context = response.json()
    if context:
        return render(request, 'blogg/weather.html', {
        "form":NewTaskForm(),
        'day': days,
        })

    else:
        return redirect('http://127.0.0.1:8000/blogg/')


