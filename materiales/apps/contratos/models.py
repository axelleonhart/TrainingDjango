from django.db import models
from apps.proveedores.models import Proveedor

# Create your models here.


class Contrato(models.Model):
    """
    Se declara el modelo contrato 
    """
    id_contrato = models.CharField(max_length=20, primary_key=True)
    monto = models.FloatField()
    rfc = models.ForeignKey(Proveedor, null=False, blank=False,
                            on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return '{}'.format(self.id_contrato)


class Movimiento(models.Model):
    """
    Se declara el modelo movimiento 
    """
    concepto = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20)
    unidad = models.CharField(max_length=20)
    contrato = models.ForeignKey(Contrato, null=False, blank=False,
                                 on_delete=models.CASCADE)
    fecha = models.DateField()
