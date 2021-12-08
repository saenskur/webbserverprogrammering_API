from django.shortcuts import redirect, render
from .forms import RegisterForm

# Create your views here.
#def register(response):
    #Person 8, här behövs kod för att skicka ett response med en form skapas (Ta hjälp av tidigare uppgiften)


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("")
    else: 
        form = RegisterForm()

    return render(response, 'templates/register.html', {"form":form})