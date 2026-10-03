from config.views import ModeloBaseViewSet

from .models import Categoria, Producto, Inventario
from .serializers import (
    CategoriaSerializer,
    ProductoSerializer,
    InventarioSerializer
)


class CategoriaViewSet(ModeloBaseViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(ModeloBaseViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class InventarioViewSet(ModeloBaseViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer