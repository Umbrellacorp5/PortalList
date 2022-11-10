from enum import unique
from django.db import models
from administracion.models import Usuario

# Create your models here.

class Profesor(Usuario):
    cargo = models.CharField(max_length=255, null=False)
    antiguedad = models.CharField(max_length=255, null=False)



class Lista(models.Model):
    codLista = models.IntegerField( null=False, unique=True)
    falta = models.BooleanField(default=False, null=False)
    justificada = models.BooleanField(default=False, null=False)
    llegada_tarde = models.BooleanField(default=False, null=False)


class Materia(models.Model):
    codMateria = models.IntegerField(null=False, unique=True)
    nombre = models.CharField(max_length=255, null=False)
    usuarioCI = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre