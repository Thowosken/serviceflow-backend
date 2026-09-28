from rest_framework import viewsets

from .models import (
    Perfil,
    Usuario,
    Cliente,
    Categoria,
    Servico,
    Observacao
)

from .serializers import (
    PerfilSerializer,
    UsuarioSerializer,
    ClienteSerializer,
    CategoriaSerializer,
    ServicoSerializer,
    ObservacaoSerializer
)


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class ObservacaoViewSet(viewsets.ModelViewSet):
    queryset = Observacao.objects.all()
    serializer_class = ObservacaoSerializer