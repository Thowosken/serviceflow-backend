from rest_framework import serializers

from .models import (
    Perfil,
    Usuario,
    Cliente,
    Categoria,
    Servico,
    Observacao
)


class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = [
            "id",
            "nome",
            "email",
            "perfil",
        ]


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = "__all__"


class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servico
        fields = "__all__"


class ObservacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Observacao
        fields = "__all__"