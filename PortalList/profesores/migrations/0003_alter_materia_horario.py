# Generated by Django 4.1.1 on 2022-10-28 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_remove_profesor_apellido_remove_profesor_cedula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='horario',
            field=models.DateTimeField(),
        ),
    ]
