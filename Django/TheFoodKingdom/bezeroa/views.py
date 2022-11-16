from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from erosketa.models import Erosketak, Saskiak

import re

from .models import Bezeroak


# Create your views here.
def profila(request):
    user = request.user
    bezeroa = Bezeroak.objects.get(id_erabiltzaile=user)

    erosketak = Erosketak.objects.filter(bezero_dni=bezeroa, bukatuta=True)

    saskiak=[]
    if erosketak:
        for eros in erosketak:
            saski = Saskiak.objects.filter(erosketa_id=eros.id)
            print(saski)
            saskiak.extend(saski)

        
        return render(request, 'profila.html', {'erosketak': erosketak, 'saskiak': saskiak, 'bezeroa': bezeroa})
    else:
        return render(request, 'profila.html')

def profilaaldatu(request, id_erabiltzaile):
    bezeroa = Bezeroak.objects.get(id_erabiltzaile=id_erabiltzaile)
    return render(request, 'profilaaldatu.html', {'bezeroa': bezeroa})


def profilaaldatudb(request, id):
    erabiltzailea = request.POST['username']
    izena = request.POST['first_name']
    abizena = request.POST['last_name']
    telefonoa = request.POST['telefono_zenbakia']

    user = User.objects.get(id=id)

    user.username = erabiltzailea
    user.first_name = izena
    user.last_name = abizena

    bezero = Bezeroak.objects.get(id_erabiltzaile=id)
    bezero.telefono_zenbakia = telefonoa

    user.save()
    bezero.save()

    return redirect('profila')


def erregistratu(request):
    erabiltzailea = request.POST['username']
    izena = request.POST['first_name']
    abizena = request.POST['last_name']
    nan = request.POST['dni']
    korreoa = request.POST['email']
    pasahitza = request.POST['password']
    pasahitza_errepikatu = request.POST['password_repeat']

    dni_pattern = "^((([A-Za-z])\d{8})|(\d{8}([A-Za-z])))$";
    pat = re.compile(dni_pattern)

    if len(pasahitza) < 6 or pasahitza.isalnum() != True:
        messages.warning(request, 'Pasahitza oso motza da eta zenbakiak eduki behar du')
        return redirect('erregistroa')

    elif pasahitza != pasahitza_errepikatu:
        messages.warning(request, 'Pasahitzak ez dira berdinak')
        return redirect('erregistroa')

    elif not izena.isalpha():
        messages.warning(request, 'Izenak ezin du zenbakirik eduki')
        return redirect('erregistroa')

    elif not abizena.isalpha():
        messages.warning(request, 'Abizenak ezin du zenbakirik eduki')
        return redirect('erregistroa')

    elif not re.fullmatch(pat, nan):
        messages.warning(request, 'NAN zenbakia ez da egokia')
        return redirect('erregistroa')

    else:
        password = make_password(pasahitza)
        erabiltzailea = User(username=erabiltzailea, first_name=izena, last_name=abizena, email=korreoa,
                             password=password)

        try:
            erabiltzailea.save()

            bezeroa = Bezeroak(dni=nan, id_erabiltzaile=erabiltzailea)
            bezeroa.save()
            return redirect('index')
        except:
            messages.warning(request, 'Erabiltzaile izen hori erabilita dago. Aukeratu beste bat')
            return redirect('erregistroa')


def erregistroa(request):
    return render(request, 'erregistroa.html')
