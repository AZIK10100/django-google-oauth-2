from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

class UserForm(RegisterForm):

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


