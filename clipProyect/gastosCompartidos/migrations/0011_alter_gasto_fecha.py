# Generated by Django 4.2.6 on 2024-08-21 00:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastosCompartidos', '0010_gasto_participantes_alter_gasto_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 20, 21, 31, 0, 175944)),
        ),
    ]
