from django.db import models

from config.models import ModeloBase


class Categoria(ModeloBase):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(ModeloBase):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos"
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    peso = models.FloatField(default=0)
    disponible = models.BooleanField(default=True)
    fecha_lanzamiento = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre


class Inventario(ModeloBase):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name="inventario"
    )
    cantidad = models.PositiveIntegerField(default=0)
    cantidad_minima = models.PositiveIntegerField(default=5)
    ultima_entrada = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Inventario de {self.producto}"