from config.views import ModeloBaseViewSet

from .models import Pedido, DetallePedido, Pago
from .serializers import (
    PedidoSerializer,
    DetallePedidoSerializer,
    PagoSerializer
)


class PedidoViewSet(ModeloBaseViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class DetallePedidoViewSet(ModeloBaseViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class PagoViewSet(ModeloBaseViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    