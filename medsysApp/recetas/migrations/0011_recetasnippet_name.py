# Generated by Django 2.2.1 on 2020-02-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0010_receta_template_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetasnippet',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]