from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput())
    password1 = forms.CharField(min_length=8,
                                max_length=80,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8,
                                max_length=80,
                                required=True,
                                widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")