from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import ProductoViewSet
from .views import lista_productos


router = DefaultRouter()
router.register(
    "productos",
    ProductoViewSet,
    basename="producto",
)

urlpatterns = [
    path("", lista_productos, name="lista_productos"),
    path("api/", include(router.urls)),
]