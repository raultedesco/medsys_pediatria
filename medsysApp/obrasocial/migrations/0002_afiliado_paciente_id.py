# Generated by Django 2.2.1 on 2019-06-04 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_remove_paciente_afiliado'),
        ('obrasocial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='afiliado',
            name='paciente_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente'),
            preserve_default=False,
        ),
    ]
