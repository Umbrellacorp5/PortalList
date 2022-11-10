from enum import unique
from django.db import models
from django.forms import ModelForm

class Administrador(models.Model):
    email = models.CharField(max_length=255, null=False, unique=True)
    contraseña = models.CharField(max_length=255, null=False)



class Usuario(models.Model):
    cedula = models.IntegerField(null=False, unique=True)
    usuario = models.CharField(max_length=255, null=False)
    nombre = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    codAdministrador = models.ForeignKey(Administrador,on_delete=models.CASCADE)

    class Meta:
        abstract = True



class Grupo(models.Model):
    nombre = models.CharField(max_length=255, null=False, unique=True)



class Pasan(models.Model):

    nombreGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    usuarioCI = models.ForeignKey(to='alumnos.Alumno', on_delete=models.CASCADE, null=False)
    codLista = models.ForeignKey(to='profesores.Lista',on_delete=models.CASCADE, null=False)
    fecha = models.DateField(null=False)



