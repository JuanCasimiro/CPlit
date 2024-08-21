# Generated by Django 4.2.6 on 2024-08-21 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastosCompartidos', '0020_rename_acreedor_deuda_creditor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deuda',
            name='state',
            field=models.CharField(choices=[('P', 'Pendiente'), ('C', 'Pagada'), ('D', 'Eliminada')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 21, 5, 1, 26, 579971)),
        ),
    ]
