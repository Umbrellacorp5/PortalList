# Generated by Django 4.1.1 on 2022-11-10 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_remove_alumno_usuario_ptr_alumno_apellido_and_more'),
        ('administracion', '0008_remove_usuario_codadministrador'),
        ('profesores', '0006_remove_profesor_usuario_ptr_profesor_apellido_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
