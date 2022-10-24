from django.db import models

from Django.TheFoodKingdom.bezeroa.models import Bezeroak
from Django.TheFoodKingdom.erosketa.models import Erosketak


# Create your models here.

class Bidalketak(models.Model):
    id = models.AutoField(primary_key=True)
    eguna = models.DateField(null=True)
    ordua = models.DateTimeField(null=True)
    helbidea = models.CharField(max_length=50)
    erosketa_id = models.ForeignKey(Erosketak, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % self.id


class Txartelak(models.Model):
    zenbakia = models.IntegerField(primary_key=True, max_length=16)
    iraungitze_data = models.DateField(null=True)
    cvv = models.IntegerField(max_length=3)
    bezero_dni = models.ForeignKey(Bezeroak, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % self.zenbakia