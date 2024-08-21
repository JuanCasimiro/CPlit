# Generated by Django 4.2.6 on 2024-08-21 00:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gastosCompartidos', '0011_alter_gasto_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gasto',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='gasto',
            old_name='titulo',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='fecha',
        ),
        migrations.AddField(
            model_name='gasto',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 20, 21, 41, 8, 471307)),
        ),
        migrations.AddField(
            model_name='gasto',
            name='pay_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gastos_pagados', to='gastosCompartidos.user'),
            preserve_default=False,
        ),
    ]
