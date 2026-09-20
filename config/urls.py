from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from usuarios.views import (
    ClienteViewSet,
    DireccionViewSet,
    PreferenciaViewSet
)
from productos.views import (
    CategoriaViewSet,
    ProductoViewSet,
    InventarioViewSet
)
from ventas.views import (
    PedidoViewSet,
    DetallePedidoViewSet,
    PagoViewSet
)
from envios.views import (
    TransportistaViewSet,
    EnvioViewSet,
    SeguimientoViewSet
)
from soporte.views import (
    TicketViewSet,
    ComentarioViewSet,
    CalificacionViewSet
)


router = routers.DefaultRouter()

router.register("clientes", ClienteViewSet)
router.register("direcciones", DireccionViewSet)
router.register("preferencias", PreferenciaViewSet)

router.register("categorias", CategoriaViewSet)
router.register("productos", ProductoViewSet)
router.register("inventarios", InventarioViewSet)

router.register("pedidos", PedidoViewSet)
router.register("detalles-pedido", DetallePedidoViewSet)
router.register("pagos", PagoViewSet)

router.register("transportistas", TransportistaViewSet)
router.register("envios", EnvioViewSet)
router.register("seguimientos", SeguimientoViewSet)

router.register("tickets", TicketViewSet)
router.register("comentarios", ComentarioViewSet)
router.register("calificaciones", CalificacionViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]