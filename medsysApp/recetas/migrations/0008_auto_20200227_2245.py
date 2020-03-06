# Generated by Django 2.2.1 on 2020-02-28 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0007_recetatemplate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetafooter',
            name='default_footer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recetaheader',
            name='default_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='receta',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
    ]
