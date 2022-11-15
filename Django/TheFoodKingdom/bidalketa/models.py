from django.db import models
from django.core.validators import RegexValidator

from bezeroa.models import Bezeroak

from erosketa.models import Erosketak




# Create your models here.

class Bidalketak(models.Model):
    id = models.AutoField(primary_key=True)
    eguna = models.DateField(null=True)
    ordua = models.TimeField(null=True)
    helbidea = models.CharField(max_length=50)
    erosketa_id = models.ForeignKey(Erosketak, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.id


class Txartelak(models.Model):
    zenbakia = models.BigIntegerField(primary_key=True)
    iraungitze_data = models.CharField(max_length=7, validators=[RegexValidator(r'^\d\d/\d\d\d\d', message="Wrong format enter")], null=False, blank=False, help_text="format: mm/aaaa")
    cvv = models.CharField(max_length=3)
    bezero_dni = models.ForeignKey(Bezeroak, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.zenbakia
