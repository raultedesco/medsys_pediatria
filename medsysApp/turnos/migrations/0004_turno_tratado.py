# Generated by Django 2.2.1 on 2020-03-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0003_auto_20200222_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='tratado',
            field=models.BooleanField(default=False),
        ),
    ]
