# Generated by Django 2.2.1 on 2020-02-22 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0007_auto_20200221_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='apgar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='eg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='pc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='talla',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tutor',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]