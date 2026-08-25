from django.core.management.base import BaseCommand

from catalogo.models import Producto


PRODUCTOS = [
    {
        "nombre": "Sofa Nido",
        "categoria": "Sala",
        "descripcion": "Sofa de tres puestos con tapizado en lino y estructura de madera.",
        "precio": 2899000,
        "imagen_url": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=900&q=80",
        "stock": 6,
        "destacado": True,
    },
    {
        "nombre": "Mesa Roble",
        "categoria": "Comedor",
        "descripcion": "Mesa circular para cuatro personas elaborada en roble natural.",
        "precio": 1699000,
        "imagen_url": "https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=900&q=80",
        "stock": 4,
        "destacado": True,
    },
    {
        "nombre": "Silla Aura",
        "categoria": "Comedor",
        "descripcion": "Silla ergonomica de diseno nordico, acabada en madera y tela bouclé.",
        "precio": 349900,
        "imagen_url": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80",
        "stock": 14,
        "destacado": False,
    },
    {
        "nombre": "Biblioteca Oslo",
        "categoria": "Estudio",
        "descripcion": "Biblioteca modular de cinco niveles para libros y objetos decorativos.",
        "precio": 1199000,
        "imagen_url": "https://images.unsplash.com/photo-1594620302200-9a762244a156?auto=format&fit=crop&w=900&q=80",
        "stock": 3,
        "destacado": False,
    },
    {
        "nombre": "Cama Luma",
        "categoria": "Dormitorio",
        "descripcion": "Cama doble con cabecero acolchado y base de madera clara.",
        "precio": 2399000,
        "imagen_url": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80",
        "stock": 5,
        "destacado": True,
    },
    {
        "nombre": "Lampara Arco",
        "categoria": "Iluminacion",
        "descripcion": "Lampara de piso con arco metalico y pantalla de tela color marfil.",
        "precio": 429900,
        "imagen_url": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=900&q=80",
        "stock": 9,
        "destacado": False,
    },
]


class Command(BaseCommand):
    help = "Crea o actualiza los productos de ejemplo en MongoDB."

    def handle(self, *args, **options):
        for datos in PRODUCTOS:
            nombre = datos["nombre"]
            actualizados = {f"set__{campo}": valor for campo, valor in datos.items()}
            Producto.objects(nombre=nombre).update_one(upsert=True, **actualizados)

        self.stdout.write(self.style.SUCCESS(f"{len(PRODUCTOS)} productos disponibles en MongoDB."))

