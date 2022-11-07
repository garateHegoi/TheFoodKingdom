from django.shortcuts import render, redirect
from django.http import JsonResponse
from janaria.models import Janariak

from .models import Saskiak

# Create your views here.
def saskia(request):
    saskia = Saskiak.objects.all
    print(saskia)
    return render(request, 'saskia.html', {'saskia':saskia})

def gehitu_saskira(request):
    id = request.POST['id']
    kop = int(request.POST.get('kop'))
    guzt = float(request.POST.get('guztira'))
    saskiak = list(Saskiak.objects.filter(janari_id_id=id))
    if saskiak:
        saskiak[0].kantitate_kopurua = kop
        saskiak[0].guztira = guzt
        saskiak[0].save()
    else:
        # Gehitu erosketa
        saskia = Saskiak(janari_id_id=id, kantitate_kopurua=kop, guztira=guzt)
        saskia.save()
    return redirect('saskia')


def ezabatu_saskia(request):
    saskia_id = int(request.POST.get('id'))
    print(saskia_id)
    saskia = Saskiak.objects.get(id=saskia_id)

    saskia_bid = list(Saskiak.objects.filter(id=saskia_id).values())

    saskia.delete()

    return JsonResponse(saskia_bid, safe=False)

def saskia_info(request, id):
    saskia = Saskiak.objects.get(id=id)
    produktua = Janariak.objects.get(id=saskia.janari_id.id)
    return render(request, 'produktua.html', {'saskia':saskia, 'produktua':produktua})


def erosketa(request):
    return render(request, 'erosketa.html')


def erosketaOrd(request):
    return render(request, 'erosketaOrd.html')
