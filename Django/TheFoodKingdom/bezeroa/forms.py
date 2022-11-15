from django import forms
from django.forms import TextInput, EmailInput

from .models import User


class LoginForm(forms.Form):
    model = User
    fields = ['username', 'password']

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'style': 'width: 300px; border-radius:', 'class': 'form-control'}))
