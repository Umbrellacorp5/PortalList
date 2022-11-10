from enum import unique
from django.db import models
from django.forms import ModelForm

class Administrador(models.Model):
    codAdministrador = models.IntegerField(primary_key=True, null=False, default=1)
    email = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)

    def __int__(self):
        return str(self.codAdministrador)


class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True, null=False)
    usuario = models.CharField(max_length=255, null=False)
    nombre = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    codAdministrador = models.ForeignKey(Administrador,on_delete=models.CASCADE)



class Grupo(models.Model):
    codGrupo = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    alumnos = models.ManyToManyField(to='alumnos.Alumno')



class Pasan(models.Model):

    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    usuarioCI = models.ForeignKey(to='alumnos.Alumno', on_delete=models.CASCADE, null=False)
    codLista = models.ForeignKey(to='profesores.Lista',on_delete=models.CASCADE, null=False)
    fecha = models.DateField(null=False)

