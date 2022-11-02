from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def profila(request):
    return render(request, 'profila.html')
    
def profilaaldatu(request):
    return render(request, 'profilaaldatu.html')


def erregistratu(request):
    erabiltzailea = request.POST['username']
    izena=request.POST['first_name']
    abizena=request.POST['last_name']
    korreoa=request.POST['email']
    pasahitza=request.POST['password']
    pasahitza_errepikatu=request.POST['password_repeat']

    if pasahitza != pasahitza_errepikatu:
        return redirect('erregistroa')
    else:
        password = make_password(pasahitza)
        erabiltzailea = User(username=erabiltzailea, first_name=izena, last_name=abizena,email=korreoa,password=password)

        erabiltzailea.save()
        return redirect('index')

    