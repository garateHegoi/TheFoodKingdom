from django import forms
from django.forms import TextInput, EmailInput

from .models import User


class LoginForm(forms.Form):
    model = User
    fields = ['username', 'password']

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Erabiltzailea',  'class': 'form-control input_form'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'form-control input_form'}))
