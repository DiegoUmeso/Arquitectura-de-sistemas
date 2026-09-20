from config.views import ModeloBaseViewSet

from .models import Cliente, Direccion, Preferencia
from .serializers import (
    ClienteSerializer,
    DireccionSerializer,
    PreferenciaSerializer
)


class ClienteViewSet(ModeloBaseViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class DireccionViewSet(ModeloBaseViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class PreferenciaViewSet(ModeloBaseViewSet):
    queryset = Preferencia.objects.all()
    serializer_class = PreferenciaSerializer