# Generated by Django 2.2.1 on 2020-02-19 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_recetafooter_recetaheader_recetasnippet_recetatemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetaheader',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos'),
        ),
    ]
