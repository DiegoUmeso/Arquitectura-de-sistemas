from django.db import models
from django.utils import timezone

from config.models import ModeloBase


class Pedido(ModeloBase):
    cliente = models.ForeignKey(
        "usuarios.Cliente",
        on_delete=models.CASCADE,
        related_name="pedidos"
    )
    estado = models.CharField(
        max_length=30,
        default="pendiente"
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    pagado = models.BooleanField(default=False)
    fecha_entrega_estimada = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Pedido {self.id}"


class DetallePedido(ModeloBase):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    producto = models.ForeignKey(
        "productos.Producto",
        on_delete=models.CASCADE,
        related_name="detalles_pedido"
    )
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    descuento = models.FloatField(default=0)

    def __str__(self):
        return f"{self.producto} - {self.cantidad}"


class Pago(ModeloBase):
    pedido = models.OneToOneField(
        Pedido,
        on_delete=models.CASCADE,
        related_name="pago"
    )
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    metodo = models.CharField(max_length=50)
    referencia = models.CharField(
        max_length=100,
        blank=True
    )
    fecha_pago = models.DateTimeField(default=timezone.now)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pago del pedido {self.pedido.id}"