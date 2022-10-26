from django.shortcuts import render

# Create your views here.
def profila(request):
    return render(request, 'profila.html')
    
def profilaaldatu(request):
    return render(request, 'profilaaldatu.html')