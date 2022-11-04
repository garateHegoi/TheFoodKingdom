from django.shortcuts import render, redirect

from .models import Saskiak

# Create your views here.
def saskia(request):
    saskia = Saskiak.objects.all
    return render(request, 'saskia.html', {'saskia':saskia})

def gehitu_saskira(request):
    id = request.POST['id']
    kop = request.POST.get('kop')
    guzt = request.POST.get('guztira')
    saskia = Saskiak(janari_id_id=id, kantitate_kopurua=kop, guztira=guzt)
    saskia.save()
    return redirect('saskia')


def ezabatu_saskia(request, id):
    saskia = Saskiak.objects.get(id=id)
    saskia.delete()
    return redirect('saskia')

