from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PerfilViewSet,
    UsuarioViewSet,
    ClienteViewSet,
    CategoriaViewSet,
    ServicoViewSet,
    ObservacaoViewSet
)


router = DefaultRouter()

router.register("perfis", PerfilViewSet)
router.register("usuarios", UsuarioViewSet)
router.register("clientes", ClienteViewSet)
router.register("categorias", CategoriaViewSet)
router.register("servicos", ServicoViewSet)
router.register("observacoes", ObservacaoViewSet)


urlpatterns = [
    path("", include(router.urls)),
]