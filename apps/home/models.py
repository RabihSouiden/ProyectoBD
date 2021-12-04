from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MASCOTA(models.Model):
    id_mascota = models.IntegerField(primary_key = True)
    edad = models.IntegerField()
    tamaño = models.IntegerField()
    nombre = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    potencialmente_peligroso = models.CharField(max_length=255)
    fotografía_medica = models.CharField(max_length=255)
    microchip = models.CharField(max_length=255)
