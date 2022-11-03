from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bezeroak(models.Model):
   dni= models.CharField(primary_key=True, max_length=9)
   telefono_zenbakia= models.CharField(max_length=9)
   posta_kodea = models.CharField(max_length=5)
   herria = models.CharField(max_length=50)
   probintzia = models.CharField(max_length=50)
   id_erabiltzaile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

   def __str__(self):
       return '%s' % self.dni
