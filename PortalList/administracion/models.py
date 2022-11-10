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



class Estan(models.Model):
    class Meta:
        unique_together = (('codGrupo', 'codAlumno'),)

    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    codAlumno = models.ForeignKey(to='alumnos.Alumno', on_delete=models.CASCADE, null=False)

'''

    class Meta:
        unique_together = (("codGrupo","codAlumno"))


    def __str__(self):
        return self.dept_id
'''
class Tienen(models.Model):
    class Meta:
        unique_together = (('codGrupo', 'codProfesor'),)

    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    codProfesor = models.ForeignKey(to='profesores.Profesor', on_delete=models.CASCADE, null=False)
   

'''
    class Meta:
        unique_together = (("codGrupo","codProfesor"))


    def __str__(self):
        return self.dept_id
'''
class Pasan(models.Model):

    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    codProfesor = models.ForeignKey(to='profesores.Profesor', on_delete=models.CASCADE, null=False)
    codLista = models.ForeignKey(to='profesores.Lista',on_delete=models.CASCADE, null=False)
    fecha = models.DateField(null=False)

