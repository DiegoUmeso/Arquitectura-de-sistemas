from rest_framework import serializers

from .models import Ticket, Comentario, Calificacion


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"


class ComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = "__all__"


class CalificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calificacion
        fields = "__all__"