from config.views import ModeloBaseViewSet

from .models import Transportista, Envio, Seguimiento
from .serializers import (
    TransportistaSerializer,
    EnvioSerializer,
    SeguimientoSerializer
)


class TransportistaViewSet(ModeloBaseViewSet):
    queryset = Transportista.objects.all()
    serializer_class = TransportistaSerializer


class EnvioViewSet(ModeloBaseViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer


class SeguimientoViewSet(ModeloBaseViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer