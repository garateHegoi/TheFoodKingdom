from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import JsonResponse
from janaria.models import Janariak

from django.contrib.auth.decorators import login_required
from .models import Erosketak, Saskiak, Txartelak, Bidalketak
from bezeroa.models import Bezeroak
from django.contrib import messages
import pandas as pd


# Create your views here.
@login_required(login_url="login")
def saskia(request):
    user = request.user
    bezeroa = Bezeroak.objects.get(id_erabiltzaile=user)

    try:
        erosketa = Erosketak.objects.get(bezero_dni=bezeroa, bukatuta=False)
        saskia = Saskiak.objects.filter(erosketa_id=erosketa.id)
        return render(request, 'saskia.html', {'saskia': saskia})
    except:
        return render(request, 'saskia.html')


@login_required(login_url="login")
def gehitu_saskira(request):
    id = request.POST['id']
    kop = int(request.POST.get('kop'))
    guzt = float(request.POST.get('guztira'))

    # Erosketa sortu
    user = request.user
    bezeroa = Bezeroak.objects.get(id_erabiltzaile=user)
    try:
        erosketa = Erosketak.objects.get(bezero_dni=bezeroa, bukatuta=False)
    except:
        erosketa = Erosketak.objects.create(bezero_dni=bezeroa, bukatuta=False)

    try:
        # Aldatu 
        saski = Saskiak.objects.get(janari_id_id=id)
        saski.kantitate_kopurua = kop
        saski.guztira = guzt
        saski.erosketa_id = erosketa
        saski.save()
    except:
        # Gehitu erosketa
        saskia = Saskiak(janari_id_id=id, kantitate_kopurua=kop, guztira=guzt, erosketa_id=erosketa)
        saskia.save()

    # Saski guztiak hartu eta guztira kalkulatu
    erosketa = Erosketak.objects.get(bezero_dni=bezeroa, bukatuta=False)
    saskiak = list(Saskiak.objects.filter(erosketa_id=erosketa.id))
    erosketa.totala = 0
    for saski in saskiak:
        erosketa.totala += saski.guztira
    erosketa.save()
    return redirect('saskia')


@login_required(login_url="login")
def ezabatu_saskia(request):
    saskia_id = int(request.POST.get('id'))

    saskia = Saskiak.objects.get(id=saskia_id)

    saskia_bid = list(Saskiak.objects.filter(id=saskia_id).values())

    erosketa = Erosketak.objects.get(id=saskia.erosketa_id_id)

    erosketa.totala -= saskia.guztira
    erosketa.save()

    saskia.delete()

    return JsonResponse(saskia_bid, safe=False)


@login_required(login_url="login")
def saskia_info(request, id):
    saskia = Saskiak.objects.get(id=id)
    produktua = Janariak.objects.get(id=saskia.janari_id.id)
    return render(request, 'produktua.html', {'saskia': saskia, 'produktua': produktua})


@login_required(login_url="login")
def erosketa(request):
    bezero = Bezeroak.objects.get(id_erabiltzaile=request.user)
    print(bezero.dni)
    return render(request, 'erosketa.html', {'bezero': bezero})


@login_required(login_url="login")
def gehitu_bezero_datuak(request):
    erabil = request.user
    bezeroa = Bezeroak.objects.get(id_erabiltzaile_id=erabil.id)

    telefonoa = request.POST['telefonoa']
    herria = request.POST['herria']
    probintzia = request.POST['probintzia']
    helbidea = request.POST['helbidea']
    pk = request.POST['ok']

    bezeroa.telefono_zenbakia = telefonoa
    bezeroa.herria = herria
    bezeroa.probintzia = probintzia
    bezeroa.helbidea = helbidea
    bezeroa.posta_kodea = pk

    bezeroa.save()

    return redirect('erosketaOrdainketa')


@login_required(login_url="login")
def erosketaOrdainketa(request):
    return render(request, 'erosketaOrdainketa.html')


@login_required(login_url="login")
def gehitu_ordainketa_datuak(request):
    erabil = request.user
    bezeroa = Bezeroak.objects.get(id_erabiltzaile_id=erabil.id)

    txartelaZbk = request.POST['txartelaZbk']
    # Formatear la data y comprobar que no está caducada
    iraungitzeData = request.POST['iraungitzeData']
    titularra = request.POST['titularra']
    cvv = request.POST['CVV']

    txartelak = Txartelak.objects.filter(bezero_dni_id=bezeroa.dni)

    today = datetime.today()
    current_year = today.year
    current_month = today.month

    if (int(iraungitzeData[:2]) > current_month and int(iraungitzeData[3:8]) == current_year) or int(iraungitzeData[3:8]) > current_year:
        if not txartelak:
            txartela = Txartelak(zenbakia=txartelaZbk, iraungitze_data=iraungitzeData, titularra=titularra, cvv=cvv,
                                 bezero_dni=bezeroa)
            txartela.save()
            return redirect('erosketaLaburpena')
        else:
            for txartela in txartelak:
                if (int(txartela.iraungitze_data[:2]) < current_month and int(txartela.iraungitze_data[3:8]) == current_year) or int(txartela.iraungitze_data[3:8]) < current_year:
                    txartela.delete()
                elif str(txartela.zenbakia) == txartelaZbk:
                    if txartela.cvv ==  cvv and txartela.titularra == titularra and txartela.iraungitze_data == iraungitzeData:
                        return redirect('erosketarenLaburpena')
                    else:
                        messages.warning(request, "CVV, titularra edo iraungitze data oker daude!!!")
                        return redirect('erosketaOrdainketa')
                        return redirect('erosketarenLaburpena')

            txartelBerriBat = Txartelak(zenbakia=txartelaZbk, iraungitze_data=iraungitzeData, titularra=titularra,
                                        cvv=cvv,
                                        bezero_dni=bezeroa)
            txartelBerriBat.save()
            return redirect('erosketarenLaburpena')
    else:
        messages.warning(request, "Txartelaren iraungitze data iraungituta dago!!!")
        return redirect('erosketaOrdainketa')

@login_required(login_url="login")
def erosketarenLaburpena(request):
    bezeroa = Bezeroak.objects.get(id_erabiltzaile=request.user)
    erosketa = Erosketak.objects.get(bezero_dni=bezeroa, bukatuta=False)
    saskia = Saskiak.objects.filter(erosketa_id = erosketa)

    gaur = datetime.today()
    orain = timezone.localtime()

    if bezeroa.herria == 'Eibar':
        final_time = orain + pd.DateOffset(minutes=20)

        try:
            bidalketa = Bidalketak.objects.get(erosketa_id_id=erosketa.id)
            bidalketa.kostua=2
            bidalketa.eguna=gaur
            bidalketa.ordua=final_time
            bidalketa.helbidea=bezeroa.helbidea
            bidalketa.herria
            bidalketa.probintzia
            bidalketa.save()
        except:
            bidalketa = Bidalketak.objects.create(erosketa_id=erosketa, kostua=2, eguna=gaur, helbidea=bezeroa.helbidea, herria=bezeroa.herria, probintzia=bezeroa.probintzia, ordua=final_time)
        
        erosketa.ordaintzeko_guztira= erosketa.totala+2
        erosketa.save()

    elif bezeroa.herria != 'Eibar' and bezeroa.probintzia == 'Gipuzkoa':
        final_time = orain + pd.DateOffset(minutes=30)

        try:
            bidalketa = Bidalketak.objects.get(erosketa_id_id=erosketa.id)
            bidalketa.kostua=3
            bidalketa.eguna=gaur
            bidalketa.ordua=final_time
            bidalketa.helbidea=bezeroa.helbidea
            bidalketa.herria
            bidalketa.probintzia
            bidalketa.save()
        except:
            bidalketa = Bidalketak.objects.create(erosketa_id=erosketa, kostua=3, eguna=gaur, helbidea=bezeroa.helbidea, herria=bezeroa.herria, probintzia=bezeroa.probintzia, ordua=final_time)
        
        erosketa.ordaintzeko_guztira= erosketa.totala+3
        erosketa.save()

    else:
        final_time = orain + pd.DateOffset(minutes=45)

        try:
            bidalketa = Bidalketak.objects.get(erosketa_id_id=erosketa.id)
            bidalketa.kostua=5
            bidalketa.eguna=gaur
            bidalketa.ordua=final_time
            bidalketa.helbidea=bezeroa.helbidea
            bidalketa.herria
            bidalketa.probintzia
            bidalketa.save()
        except:
            bidalketa = Bidalketak.objects.create(erosketa_id=erosketa, kostua=5, eguna=gaur, helbidea=bezeroa.helbidea, herria=bezeroa.herria, probintzia=bezeroa.probintzia, ordua=final_time)
        
        erosketa.ordaintzeko_guztira= erosketa.totala+5
        erosketa.save()

    return render(request, 'erosketarenLaburpena.html', {'bezeroa': bezeroa, 'erosketa':erosketa, 'saskia': saskia, 'bidalketa': bidalketa})

@login_required(login_url="login")
def erosketa_bukatu(request):
    bezeroa = Bezeroak.objects.get(id_erabiltzaile=request.user)
    erosketa = Erosketak.objects.get(bezero_dni=bezeroa, bukatuta=False)
    erosketa.bukatuta = True
    erosketa.eguna = datetime.today()
    erosketa.ordua = timezone.localtime()

    erosketa.save()

    bezeroa.puntuak+=(erosketa.totala*100)/10
    bezeroa.save()

    return redirect('index')

@login_required(login_url="login")
def puntuak_trukatu(request):
    bezeroa = Bezeroak.objects.get(id_erabiltzaile=request.user)
    erosketa = Erosketak.objects.get(bezero_dni=bezeroa, bukatuta=False)
    puntuak = bezeroa.puntuak

    deskontua= puntuak/100
    erosketa.ordaintzeko_guztira=float(erosketa.ordaintzeko_guztira)-deskontua
    erosketa.save()
    
    bezeroa.puntuak=0
    bezeroa.save()


    return JsonResponse({'puntuak':puntuak, 'deskontua':deskontua},status=200)