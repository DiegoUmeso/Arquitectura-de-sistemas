import uuid

from django.db import models
from django.utils import timezone


class ModeloBase(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    eliminado = models.BooleanField(default=False)
    fecha_eliminacion = models.DateTimeField(
        null=True,
        blank=True
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def eliminar(self):
        self.eliminado = True
        self.fecha_eliminacion = timezone.now()
        self.save()