from django.db import models

# Create your models here.

class Janariak(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=50)
    osagaiak = models.CharField(max_length=100, blank=True)
    prezioa = models.CharField(max_length=5)
    mota = models.CharField(max_length=50)
    submota=models.CharField(max_length=50, null=True)
    alergenoak = models.CharField(max_length=50)
    argazki_url = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.izena
