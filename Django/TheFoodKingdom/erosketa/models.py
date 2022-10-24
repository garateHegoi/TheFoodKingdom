from django.db import models

from TheFoodKingdom.bezeroak.models import Bezeroak
from TheFoodKingdom.janariak.models import Janariak


# Create your models here.


class Saskiak(models.Model):
    id = models.AutoField(primary_key=True)
    kantitate_kopurua = models.CharField(max_length=50)
    janari_id = models.ForeignKey(Janariak, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.id

#erosketa

class Erosketak(models.Model):
    id = models.AutoField(primary_key=True)
    eguna = models.DateField(null=True)
    ordua = models.DateTimeField(null=True)
    ordaintzeko_guztira = models.IntegerField(max_length=5)
    bezero_dni = models.ForeignKey(Bezeroak, on_delete=models.CASCADE)
    saskia_id = models.ForeignKey(Saskiak, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.id