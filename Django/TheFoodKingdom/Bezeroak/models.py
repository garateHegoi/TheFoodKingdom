from django.db import models

from Django.TheFoodKingdom.Janariak.models import Janariak


# Create your models here.

# Bezeroak

class Bezeroak(models.Model):
   dni= models.CharField(primary_key=True, max_length=50)
   izena= models.CharField(max_length=50)
   abizena= models.CharField(max_length=50)
   helbidea= models.CharField(max_length=50)
   telefono_zenbakia= models.IntegerField(max_length=9)
   pk = models.IntegerField(max_length=5)
   herria = models.CharField(max_length=50)
   probintzia = models.CharField(max_length=50)
   janari_id= models.ForeignKey(Janariak, on_delete=models.CASCADE)

   def __str__(self):
       return '%s' % self.izena


# Erabiltzaileak

class Erabiltzaileak(models.Model):
   id = models.AutoField(primary_key=True)
   password = models.CharField(max_length=50)
   last_login = models.CharField(max_length=50)
   is_superuser = models.CharField(max_length=50)
   username = models.CharField(max_length=50)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   email = models.CharField(max_length=50)
   is_staff = models.CharField(max_length=50)
   is_active = models.CharField(max_length=50)
   date_joinded = models.CharField(max_length=50)
   bezero_dni = models.ForeignKey(Bezeroak, on_delete=models.CASCADE)

   def __str__(self):
       return '%s' % self.username

# Txartela

class Txartelak(models.Model):
    zenbakia = models.IntegerField(primary_key=True, max_length=16)
    iraungitze_data = models.DateField(null=True)
    cvv = models.IntegerField(max_length=3)
    bezero_dni = models.ForeignKey(Bezeroak, on_delete=models.CASCADE)

def __str__(self):
    return '%s' % self.zenbakia
