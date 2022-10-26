from django import forms

from .models import Erabiltzaileak

class ErregistroaForm(forms.ModelForm):

    class Meta:
        model = Erabiltzaileak
        fields = ('username', 'email','first_name','last_name','password')