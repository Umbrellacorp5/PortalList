from django.db import models
from django.forms import ModelForm
from administracion.models import Usuario

# Create your models here.


class Alumno(Usuario):
    usuarioci = models.ForeignKey(to='administracion.Usuario', on_delete=models.CASCADE, null=False)
    numPadre = models.CharField(max_length=255, null=False)
    fotoAlumno = models.ImageField(upload_to="Alumno")
    mac = models.CharField(max_length=255)

    def __int__(self):
        return str(self.codAlumno + ' ' + self.usuarioci)
'''
class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'alumnos']
'''