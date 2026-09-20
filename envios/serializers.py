from rest_framework import serializers

from .models import Transportista, Envio, Seguimiento


class TransportistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transportista
        fields = "__all__"


class EnvioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envio
        fields = "__all__"


class SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seguimiento
        fields = "__all__"