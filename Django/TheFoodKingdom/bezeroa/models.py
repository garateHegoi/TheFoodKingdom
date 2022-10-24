from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Bezeroak(models.Model):
   dni= models.CharField(primary_key=True, max_length=50)
   telefono_zenbakia= models.IntegerField(validators=[
        MinValueValidator(9), MaxValueValidator(9)])
   posta_kodea = models.IntegerField(validators=[
        MinValueValidator(5), MaxValueValidator(5)])
   herria = models.CharField(max_length=50)
   probintzia = models.CharField(max_length=50)

   def __str__(self):
       return '%s' % self.izena


# Erabiltzailea

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
   bezero_dni = models.ForeignKey(Bezeroak, on_delete=models.CASCADE, null=True)

   def __str__(self):
       return '%s' % self.username