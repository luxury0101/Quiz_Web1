from mongoengine import BooleanField, Document, FloatField, IntField, StringField


class Producto(Document):
    """Documento de un mueble almacenado en la coleccion productos."""

    nombre = StringField(required=True, max_length=120)
    categoria = StringField(required=True, max_length=80)
    descripcion = StringField(required=True, max_length=400)
    precio = FloatField(required=True, min_value=0)
    imagen_url = StringField(required=True)
    stock = IntField(required=True, min_value=0)
    destacado = BooleanField(default=False)

    meta = {
        "collection": "productos",
        "ordering": ["-destacado", "nombre"],
        "indexes": ["categoria", "nombre"],
    }

