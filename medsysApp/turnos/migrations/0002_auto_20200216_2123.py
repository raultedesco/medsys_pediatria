# Generated by Django 2.2.1 on 2020-02-17 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='paciente_id',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente'),
        ),
    ]
