# Generated by Django 2.2.1 on 2020-02-28 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0009_auto_20200228_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='template_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recetas.RecetaTemplate'),
            preserve_default=False,
        ),
    ]