
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUsers(AbstractUser):
    num_documento = models.IntegerField(primary_key = True)
    tipo_documento = models.IntegerField()
    tipo_usuario = models.IntegerField()
    username = models.CharField(max_length=255, unique=True)
    telefono_usuario = models.CharField(max_length=255)
    email = models.EmailField()
    password1 = models.CharField(max_length=255)
    direccion_usuario = models.CharField(max_length=255)
    barrio_usuario = models.CharField(max_length=255)
    localidad_usuario = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

