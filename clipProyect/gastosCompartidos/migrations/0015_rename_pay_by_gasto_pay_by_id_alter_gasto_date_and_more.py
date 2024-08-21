# Generated by Django 4.2.6 on 2024-08-21 06:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('gastosCompartidos', '0014_alter_gasto_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gasto',
            old_name='pay_by',
            new_name='pay_by_id',
        ),
        migrations.AlterField(
            model_name='gasto',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 21, 3, 44, 58, 126754)),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name='Deuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('C', 'Pagada'), ('D', 'Eliminada')], default='D', max_length=1)),
                ('fecha_pago', models.DateTimeField(blank=True, null=True)),
                ('acreedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deudas_como_acreedor', to='users.user')),
                ('debedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deudas_como_debedor', to='users.user')),
                ('gasto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gasto', to='gastosCompartidos.gasto')),
            ],
        ),
    ]
