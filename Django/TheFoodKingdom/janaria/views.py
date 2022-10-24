from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index_bueltatu(request):
    
    return redirect('index')

def karta(request):
    return render(request, 'karta.html')

def kokapena(request):
    return render(request, 'kokapena.html')