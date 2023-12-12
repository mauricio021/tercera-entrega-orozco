from django.db import models


class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"