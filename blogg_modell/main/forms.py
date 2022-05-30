from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

stringLabel="Input number of days to forecast (Numbers from 1 to 10)"
class NewTaskForm (forms.Form):
    city = forms.CharField(label="")
    days = forms.IntegerField(min_value=1, max_value=3, label="")
    #max value upp till 10 men den verkar inte funka längre på webbsidan så ta max 3 för nu
