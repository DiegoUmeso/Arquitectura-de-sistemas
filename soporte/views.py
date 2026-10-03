from config.views import ModeloBaseViewSet

from .models import Ticket, Comentario, Calificacion
from .serializers import (
    TicketSerializer,
    ComentarioSerializer,
    CalificacionSerializer
)


class TicketViewSet(ModeloBaseViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ComentarioViewSet(ModeloBaseViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class CalificacionViewSet(ModeloBaseViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer