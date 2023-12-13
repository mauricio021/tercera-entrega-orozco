from django.db import models


class Productos(models.Model):
    vendedor = models.CharField(max_length=100)  
    producto = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=2, max_digits=100)
    correo = models.EmailField(max_length=254, blank=True, null=True)    

    def __str__(self):
        return f"{self.vendedor}-{self.producto} (${self.precio})"
    
