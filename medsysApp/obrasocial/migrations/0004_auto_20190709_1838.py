# Generated by Django 2.2.1 on 2019-07-09 18:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('obrasocial', '0003_auto_20190708_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='afiliado',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2019, 7, 9, 18, 37, 47, 112341, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='afiliado',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='obrasocial',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2019, 7, 9, 18, 37, 57, 997610, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obrasocial',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
