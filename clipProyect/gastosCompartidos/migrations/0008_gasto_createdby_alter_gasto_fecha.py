# Generated by Django 4.2.6 on 2024-08-20 23:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gastosCompartidos', '0007_rename_persona_user_alter_gasto_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='createdBy',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gastosCompartidos.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gasto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 20, 20, 28, 38, 61572)),
        ),
    ]
