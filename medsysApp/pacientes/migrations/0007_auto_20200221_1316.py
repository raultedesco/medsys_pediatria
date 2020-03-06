# Generated by Django 2.2.1 on 2020-02-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_auto_20190605_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='apgar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='eg',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='pc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='talla',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='tutor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='celular',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cp',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nac',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='mail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nya',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre y Apellido'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='peso_nac',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
