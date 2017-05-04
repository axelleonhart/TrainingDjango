from django.db import models
from apps.clientes.choices import SEXO_CHOICES
# Create your models here.


class Cliente(models.Model):
    """
    Se declara el modelo cliente
    """
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(choices=SEXO_CHOICES, default=1, max_length=10)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    fecha_nac = models.DateField()

    def __str__(self):
        return '{}'.format(self.nombre)


class Notas(models.Model):
    """
    Se declara el modelo notas
    """
    cliente = models.ForeignKey(Cliente, null=False, blank=False,
                                on_delete=models.CASCADE)
    monto = models.IntegerField()
    fecha_nota = models.DateField()
    contenido = models.TextField(null=True)

    def __str__(self):
        return '{}'.format(self.cliente)
