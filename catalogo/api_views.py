from bson import ObjectId
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ViewSet):

    def obtener_producto(self, pk):
        if not ObjectId.is_valid(pk):
            raise NotFound("Identificador de producto inválido.")

        producto = Producto.objects(id=pk).first()

        if producto is None:
            raise NotFound("Producto no encontrado.")

        return producto

    def list(self, request, **kwargs):
        productos = Producto.objects()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        producto = self.obtener_producto(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        producto = Producto(**serializer.validated_data).save()

        return Response(
            ProductoSerializer(producto).data,
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None, partial=False, **kwargs):
        producto = self.obtener_producto(pk)

        serializer = ProductoSerializer(
            producto,
            data=request.data,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)

        for campo, valor in serializer.validated_data.items():
            setattr(producto, campo, valor)

        producto.save()

        return Response(ProductoSerializer(producto).data)

    def partial_update(self, request, pk=None, **kwargs):
        return self.update(request, pk=pk, partial=True)

    def destroy(self, request, pk=None, **kwargs):
        producto = self.obtener_producto(pk)
        producto.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)