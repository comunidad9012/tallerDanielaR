from ast import Delete
from tabnanny import verbose
from django.db import models

# Create your models here.



class Moto(models.Model):
    id = models.AutoField(primary_key = True)
    patente = models.CharField(max_length = 100, verbose_name='Patente')
    cliente = models.CharField(max_length = 100, verbose_name='Cliente')
    vehiculo = models.CharField(max_length = 100, verbose_name='Vehiculo')
    descripcion = models.TextField(verbose_name='Descripcion', null = True)


    def __str__(self):
        fila = "Patente: " + self.patente + " - " + "Descripcion: " + self.descripcion
        return fila

    