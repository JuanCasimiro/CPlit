from django.db import models

import datetime

class persona(models.Model):

    name = models.CharField(max_length=255, null=False)
    alias = models.CharField(max_length=30)
    balance =  models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    
    def __str__(self):
        return self.name
    
class gasto(models.Model):

    titulo = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    fecha = models.DateTimeField(null=False, default= datetime.datetime.now())
    
    def __str__(self):
        return self.titulo
