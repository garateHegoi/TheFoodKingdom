from django.shortcuts import render

# Create your views here.


def saskia(request):
    return render(request, 'saskia.html')


def erosketa(request):
    return render(request, 'erosketa.html')


def erosketaOrd(request):
    return render(request, 'erosketaOrd.html')
