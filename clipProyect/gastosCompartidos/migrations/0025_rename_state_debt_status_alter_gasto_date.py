# Generated by Django 4.2.6 on 2024-08-21 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastosCompartidos', '0024_alter_gasto_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debt',
            old_name='state',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='gasto',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 21, 6, 19, 54, 325806)),
        ),
    ]
