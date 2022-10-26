from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def karta(request):
    return render(request, 'karta.html')

def kokapena(request):
    return render(request, 'kokapena.html')

def erregistroa(request):
    return render(request, 'erregistroa.html')

def profila(request):
    return render(request, 'profila.html')

def saskia(request):
    return render(request, 'saskia.html')