from datetime import datetime
from time import strftime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from bezeroa.models import Bezeroak
from django.forms import DateInput

from erosketa.models import Erosketak




# Create your models here.

class Bidalketak(models.Model):
    id = models.AutoField(primary_key=True)
    eguna = models.DateField(null=True)
    ordua = models.DateTimeField(null=True)
    helbidea = models.CharField(max_length=50)
    erosketa_id = models.ForeignKey(Erosketak, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.helbidea


class Txartelak(models.Model):
    zenbakia = models.IntegerField(primary_key=True)
    iraungitze_data = models.DateField(null=True)
    cvv = models.CharField(max_length=3)
    bezero_dni = models.ForeignKey(Bezeroak, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.zenbakia
