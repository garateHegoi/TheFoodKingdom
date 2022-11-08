from django.shortcuts import render, redirect
from django.http import JsonResponse
from janaria.models import Janariak
import uuid
from .models import Erosketak, Saskiak

# Create your views here.
def saskia(request):
    erosketak= list(Erosketak.objects.filter(session_id=request.session['nonuser']))

    if erosketak:
        saskia = Saskiak.objects.filter(erosketa_id=erosketak[0].id)
        return render(request, 'saskia.html', {'saskia':saskia})
    else:
        return render(request, 'saskia.html')

def gehitu_saskira(request):
    id = request.POST['id']
    kop = int(request.POST.get('kop'))
    guzt = float(request.POST.get('guztira'))

    # Erosketa sortu
    try:
        erosketa= Erosketak.objects.get(session_id=request.session['nonuser'])
    except:
        request.session['nonuser'] = str(uuid.uuid4())
        erosketa= Erosketak.objects.create(session_id=request.session['nonuser'])
    print(erosketa)

    saski = list(Saskiak.objects.filter(janari_id_id=id))
    if saski:
        # Aldatu erosketa
        saski[0].kantitate_kopurua = kop
        saski[0].guztira = guzt
        saski[0].erosketa_id=erosketa
        saski[0].save()
    else:
        # Gehitu erosketa
        saskia = Saskiak(janari_id_id=id, kantitate_kopurua=kop, guztira=guzt, erosketa_id=erosketa)
        saskia.save()
    
    # Saski guztiak hartu eta guztira kalkulatu
    saskiak = list(Saskiak.objects.all())
    erosketa.ordaintzeko_guztira=0 
    for x in saskiak:   
        erosketa.ordaintzeko_guztira+= x.guztira
    erosketa.save()
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


def erosketaOrdainketa(request):
    return render(request, 'erosketaOrdainketa.html')
