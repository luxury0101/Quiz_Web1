from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from mongoengine.connection import get_connection
from pymongo.errors import PyMongoError

from .apps import conectar_mongodb
from .models import Producto


def lista_productos(request) -> HttpResponse:
    """Renderiza los productos de MongoDB usando una plantilla HTML."""
    try:
        if settings.MONGODB_CONNECTION_ERROR:
            settings.MONGODB_CONNECTION_ERROR = conectar_mongodb()
        if settings.MONGODB_CONNECTION_ERROR:
            raise PyMongoError(settings.MONGODB_CONNECTION_ERROR)

        # Fuerza una comprobacion de conectividad antes de consultar la coleccion.
        get_connection().admin.command("ping")
        productos = Producto.objects()
        return render(request, "catalogo/productos.html", {"productos": productos})
    except PyMongoError:
        mensaje = (
            "No fue posible conectar con MongoDB. Verifica MONGODB_URI, "
            "la IP permitida en Atlas y las credenciales."
        )
        return render(
            request,
            "catalogo/productos.html",
            {"productos": [], "error_conexion": mensaje},
            status=503,
        )
