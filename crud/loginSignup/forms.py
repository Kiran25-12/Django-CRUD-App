from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userdata

class SignupForm(forms.ModelForm):
    class Meta:
        model = userdata
        fields = ['username', 'password1', 'password2','image']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password'}))
    
    
    