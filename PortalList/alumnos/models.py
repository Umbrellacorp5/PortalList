from django.db import models
from django.forms import ModelForm
from administracion.models import Usuario, Grupo

# Create your models here.


class Alumno(Usuario):
    numPadre = models.CharField(max_length=255, null=False)
    fotoAlumno = models.ImageField(upload_to="Alumno")
    mac = models.CharField(max_length=255)
    nombreGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

