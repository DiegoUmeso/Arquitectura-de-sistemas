from django.db import models
from django.utils import timezone

from config.models import ModeloBase


class Transportista(ModeloBase):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    sitio_web = models.URLField(blank=True)
    tarifa_base = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Envio(ModeloBase):
    pedido = models.OneToOneField(
        "ventas.Pedido",
        on_delete=models.CASCADE,
        related_name="envio"
    )
    transportista = models.ForeignKey(
        Transportista,
        on_delete=models.CASCADE,
        related_name="envios"
    )
    codigo_rastreo = models.CharField(max_length=100)
    direccion_entrega = models.TextField()
    costo = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    fecha_salida = models.DateTimeField(
        null=True,
        blank=True
    )
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return self.codigo_rastreo


class Seguimiento(ModeloBase):
    envio = models.ForeignKey(
        Envio,
        on_delete=models.CASCADE,
        related_name="seguimientos"
    )
    estado = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=150)
    fecha = models.DateTimeField(default=timezone.now)
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"{self.envio} - {self.estado}"