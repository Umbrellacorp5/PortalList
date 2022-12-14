# Generated by Django 4.1.1 on 2022-11-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_remove_usuario_codadministrador'),
        ('profesores', '0005_rename_cod_profesor_materia_usuarioci_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='usuario_ptr',
        ),
        migrations.AddField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='cedula',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='codAdministrador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administracion.administrador'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='contraseña',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='usuario',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
