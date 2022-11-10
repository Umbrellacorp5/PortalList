# Generated by Django 4.1.1 on 2022-11-10 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_alter_tienen_unique_together_remove_tienen_codgrupo_and_more'),
        ('alumnos', '0003_alter_alumno_fotoalumno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='codAlumno',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='usuarioci',
        ),
        migrations.AddField(
            model_name='alumno',
            name='nombreGrupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administracion.grupo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='usuario_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.usuario'),
            preserve_default=False,
        ),
    ]
