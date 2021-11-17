from django.forms.forms import Form
from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms

# Create your views here.
tasklist=[]
class NewTaskForm (forms.Form):
    task = forms.CharField(label="Add task")


def home(request):
    return render(request, 'index2.html')

def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasklist.append(task)
            return render(request, 'index2.html', {
                'tasklist':tasklist,
                'form':form
            })
        else:
            return render(request, 'index2.html', {
                "form":form 
            })
    return render(request, 'index2.html', {
        "form":NewTaskForm(),
        "tasklist":tasklist
    })