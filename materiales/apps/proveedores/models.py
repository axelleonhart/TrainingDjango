from django.db import models

# Create your models here.


class Proveedor(models.Model):
    """
    Se declara el modelo proveedor 
    """
    nombre = models.CharField(max_length=50)
    rfc = models.CharField(max_length=15, primary_key=True)
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)
