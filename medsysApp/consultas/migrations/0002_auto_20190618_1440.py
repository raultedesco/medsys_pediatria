# Generated by Django 2.2.1 on 2019-06-18 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_auto_20190605_1148'),
        ('consultas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.CharField(max_length=45)),
                ('perimetro_encef', models.CharField(max_length=45)),
                ('talla', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_consulta', models.DateField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]