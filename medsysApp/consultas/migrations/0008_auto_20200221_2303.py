# Generated by Django 2.2.1 on 2020-02-22 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0007_auto_20200216_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha_consulta',
            field=models.DateField(auto_now_add=True),
        ),
    ]
