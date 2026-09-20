from django.db import models

from config.models import ModeloBase


class Cliente(ModeloBase):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=25)
    numero_documento = models.CharField(
        max_length=25,
        blank=True,
        default=""
    )
    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Direccion(ModeloBase):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="direcciones"
    )
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(
        max_length=10,
        blank=True
    )
    principal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente} - {self.ciudad}"


class Preferencia(ModeloBase):
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name="preferencia"
    )
    recibir_ofertas = models.BooleanField(default=True)
    idioma = models.CharField(
        max_length=20,
        default="español"
    )
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return f"Preferencias de {self.cliente}"