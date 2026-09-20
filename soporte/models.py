from django.db import models

from config.models import ModeloBase


class Ticket(ModeloBase):
    cliente = models.ForeignKey(
        "usuarios.Cliente",
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    asunto = models.CharField(max_length=150)
    descripcion = models.TextField()
    prioridad = models.PositiveSmallIntegerField(default=1)
    cerrado = models.BooleanField(default=False)

    def __str__(self):
        return self.asunto


class Comentario(ModeloBase):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )
    autor = models.CharField(max_length=100)
    mensaje = models.TextField()
    interno = models.BooleanField(default=False)

    def __str__(self):
        return f"Comentario de {self.autor}"


class Calificacion(ModeloBase):
    cliente = models.ForeignKey(
        "usuarios.Cliente",
        on_delete=models.CASCADE,
        related_name="calificaciones"
    )
    producto = models.ForeignKey(
        "productos.Producto",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="calificaciones"
    )
    puntuacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)
    recomendaria = models.BooleanField(default=True)
    fecha_experiencia = models.DateField()

    def __str__(self):
        return f"Calificación: {self.puntuacion}"