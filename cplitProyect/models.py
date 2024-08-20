from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    personas = models.ManyToManyField(Persona, related_name='gastos')

    def __str__(self):
        return f"{self.descripcion} - ${self.monto}"

class Pago(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.persona.nombre} - ${self.monto} por {self.gasto.descripcion}"
