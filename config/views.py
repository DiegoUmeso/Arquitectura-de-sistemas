from rest_framework import viewsets


class ModeloBaseViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return super().get_queryset().filter(eliminado=False)

    def perform_destroy(self, instance):
        instance.eliminar()