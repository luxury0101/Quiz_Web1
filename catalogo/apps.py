from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from mongoengine import connect
from pymongo.errors import PyMongoError


def conectar_mongodb():
    """Conecta a Atlas y devuelve un mensaje si la red no esta disponible."""
    if not settings.MONGODB_URI:
        raise ImproperlyConfigured(
            "Falta MONGODB_URI. Crea un archivo .env a partir de .env.example."
        )

    try:
        connect(
            host=settings.MONGODB_URI,
            alias="default",
            uuidRepresentation="standard",
            serverSelectionTimeoutMS=5000,
        )
    except PyMongoError as error:
        return str(error)
    return None


class CatalogoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "catalogo"

    def ready(self):
        # La vista reintentara la conexion si Atlas no esta disponible al inicio.
        settings.MONGODB_CONNECTION_ERROR = conectar_mongodb()
