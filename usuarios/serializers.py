from rest_framework import serializers

from .models import Cliente, Direccion, Preferencia


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = "__all__"


class DireccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direccion
        fields = "__all__"


class PreferenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preferencia
        fields = "__all__"