# Generated by Django 2.2.1 on 2019-06-18 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0006_auto_20190605_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('paciente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
            ],
        ),
    ]
