from django.db import models

class User(models.Model):

    name = models.CharField(max_length=255, null=False)
    alias = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    
    def __str__(self):
        return self.name
