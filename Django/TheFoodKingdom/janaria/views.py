from django.shortcuts import render
from .models import Janariak

# Create your views here.
def index(request):
    return render(request, 'index.html')

def karta(request):
    janariak = Janariak.objects.all()
    return render(request, 'karta.html',{'janariak':janariak})

def karta_sailkatua(request, submota):
    janariak = Janariak.objects.filter(submota=submota)
    return render(request, 'karta.html',{'janariak':janariak})

def kokapena(request):
    return render(request, 'kokapena.html')

def erregistroa(request):
    return render(request, 'erregistroa.html')

def profila(request):
    return render(request, 'profila.html')

def saskia(request):
    return render(request, 'saskia.html')