# Generated by Django 4.2.6 on 2024-08-20 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastosCompartidos', '0006_gasto_rename_person_persona_delete_gast'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Persona',
            new_name='User',
        ),
        migrations.AlterField(
            model_name='gasto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 20, 20, 25, 42, 894764)),
        ),
    ]
