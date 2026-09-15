from rest_framework import serializers


class ProductoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    nombre = serializers.CharField(max_length=120)
    categoria = serializers.CharField(max_length=80)
    descripcion = serializers.CharField(max_length=400)
    precio = serializers.FloatField(min_value=0)
    imagen_url = serializers.URLField()
    stock = serializers.IntegerField(min_value=0)
    destacado = serializers.BooleanField(required=False)