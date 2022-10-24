from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def karta(request):
    return render(request, 'karta.html')