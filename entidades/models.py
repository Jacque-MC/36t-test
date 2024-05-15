from django.db import models
from django.core.validators import MinValueValidator


class Maestro(models.Model):
    nombre_completo = models.CharField(max_length=100, default="nombre default")
    sueldo = models.DecimalField(decimal_places=2,
                                 max_digits=8,
                                 default=1000)


class Salon(models.Model):
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE,
                                related_name="salones")
    codigo = models.CharField(max_length=3)
    letra = models.CharField(max_length=100, default="A")
