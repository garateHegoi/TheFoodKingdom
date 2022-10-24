from django.db import models

from TheFoodKingdom.erosketa.models import Erosketak


# Create your models here.

class Bidalketak(models.Model):
    id = models.AutoField(primary_key=True)
    eguna = models.DateField(null=True)
    ordua = models.DateTimeField(null=True)
    helbidea = models.CharField(max_length=50)
    erosketa_id = models.ForeignKey(Erosketak, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.id