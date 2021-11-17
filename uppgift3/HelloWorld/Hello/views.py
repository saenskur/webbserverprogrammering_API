from django.http.response import HttpResponse
from django.shortcuts import render



# Create your views here.
def cool(request):
    return HttpResponse('<h1> Hello guys, this is my response</h1>'
    '<a href="http://127.0.0.1:8000/Hello/home/">Home Page</a><br>'
    '<a href="http://127.0.0.1:8000/Hello/about/">About Page</a><br>'
    '<a href="http://127.0.0.1:8000/Hello/contact/">Contact Page</a>'
    )

def home(request):
    return render(request, 'index.html', {"pageTitle":"Index"})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def greet(request, name):
    return render(request, 'index.html', {"lista":["banan","apelsin", "äpple","godis","läsk"], "name":name})

def Extra(request):
    return render(request, 'extra.html')

def Forms(request):
    return render(request, 'Forms.html')