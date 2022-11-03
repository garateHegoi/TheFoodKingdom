from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login

from .models import Bezeroak

# Create your views here.
def profila(request):
    return render(request, 'profila.html')
    
def profilaaldatu(request, id_erabiltzaile):
    bezeroa= Bezeroak.objects.get(id_erabiltzaile=id_erabiltzaile)
    return render(request, 'profilaaldatu.html',{'bezeroa':bezeroa})

def profilaaldatudb(request, id):
    erabiltzailea = request.POST['username']
    izena=request.POST['first_name']
    abizena=request.POST['last_name']
    telefonoa=request.POST['telefono_zenbakia']

    user= User.objects.get(id=id)

    user.username=erabiltzailea
    user.first_name=izena
    user.last_name=abizena

    bezero= Bezeroak.objects.get(id_erabiltzaile=id)
    bezero.telefono_zenbakia=telefonoa

    user.save()
    bezero.save()

    return redirect('profila')

def erregistratu(request):
    erabiltzailea = request.POST['username']
    izena=request.POST['first_name']
    abizena=request.POST['last_name']
    nan=request.POST['dni']
    korreoa=request.POST['email']
    pasahitza=request.POST['password']
    pasahitza_errepikatu=request.POST['password_repeat']

    if pasahitza != pasahitza_errepikatu:
        return redirect('erregistroa')
    else:
        password = make_password(pasahitza)
        erabiltzailea = User(username=erabiltzailea, first_name=izena, last_name=abizena,email=korreoa,password=password)

        erabiltzailea.save()

        bezeroa = Bezeroak(dni=nan, id_erabiltzaile=erabiltzailea)
        bezeroa.save()
        return redirect('index')

    