from django.shortcuts import render, redirect

from bezeroa.forms import LoginForm
from django.http import JsonResponse
from .models import Janariak
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html',{'user':request.user})

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form=LoginForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('index')

def karta(request):
    janariak = Janariak.objects.all()
    return render(request, 'karta.html',{'janariak':janariak})

def karta_sailkatua(request):
    submota = request.POST.get('submota')
    janariak = list(Janariak.objects.filter(submota=submota).values())
    return JsonResponse(janariak,safe=False)

def kokapena(request):
    return render(request, 'kokapena.html')

def erregistroa(request):
    return render(request, 'erregistroa.html')

def profila(request):
    return render(request, 'profila.html')

def saskia(request):
    return render(request, 'saskia.html')

def produktua(request, id):
    produktua=Janariak.objects.get(id=id)
    return render(request, 'produktua.html',{'produktua':produktua})

def erosketa(request):
    return render(request, 'erosketa.html')

