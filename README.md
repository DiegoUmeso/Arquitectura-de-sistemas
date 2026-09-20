# API de tienda con Django

API sencilla desarrollada con Django y Django REST Framework. El proyecto contiene cinco aplicaciones y quince modelos relacionados.

Todos los modelos utilizan UUID como llave primaria e incluyen campos para soft delete, fecha de creación y fecha de modificación.

## Aplicaciones y modelos

- usuarios: Cliente, Direccion y Preferencia.
- productos: Categoria, Producto e Inventario.
- ventas: Pedido, DetallePedido y Pago.
- envios: Transportista, Envio y Seguimiento.
- soporte: Ticket, Comentario y Calificacion.

## Tecnologías utilizadas

- Python 3.14
- Django 6.1
- Django REST Framework
- SQLite

No es necesario configurar PostgreSQL ni otro servidor de base de datos.

## Instrucciones de instalación

### 1. Crear el entorno virtual

```powershell
python -m venv venv