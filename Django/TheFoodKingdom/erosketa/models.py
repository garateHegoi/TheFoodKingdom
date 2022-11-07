from django.db import models
from django.core.validators import MinValueValidator

from bezeroa.models import Bezeroak
from janaria.models import Janariak


# Create your models here.
class Erosketak(models.Model):
    id = models.AutoField(primary_key=True)
    eguna = models.DateField(null=True)
    ordua = models.DateTimeField(null=True)
    ordaintzeko_guztira = models.IntegerField(validators=[
        MinValueValidator(0)])
    bezero_dni = models.ForeignKey(Bezeroak, on_delete=models.CASCADE, null=True)
    #saskia_id = models.ForeignKey(Saskiak, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % self.eguna

class Saskiak(models.Model):
    id = models.AutoField(primary_key=True)
    kantitate_kopurua = models.IntegerField(validators=[
        MinValueValidator(0)])
    guztira = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    janari_id = models.ForeignKey(Janariak, on_delete=models.CASCADE)
    erosketa_id= models.ForeignKey(Erosketak, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return '%s' % self.id