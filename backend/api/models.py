from django.db import models


class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = "perfis"
        managed = False

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.DO_NOTHING,
        db_column="perfil_id"
    )

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    class Meta:
        db_table = "usuarios"
        managed = False

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = "clientes"
        managed = False

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = "categorias"
        managed = False

    def __str__(self):
        return self.nome

# SERVIÇOS

class Servico(models.Model):
    id = models.AutoField(primary_key=True)

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.DO_NOTHING,
        db_column="cliente_id"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        db_column="categoria_id"
    )

    criado_por = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        db_column="criado_por",
        related_name="servicos_criados"
    )

    tecnico = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        db_column="tecnico_id",
        related_name="servicos_atribuidos",
        null=True,
        blank=True
    )

    prioridade = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        default="ABERTO"
    )

    data_abertura = models.DateField(
        auto_now_add=False,
        null=True
    )

    class Meta:
        db_table = "servicos"
        managed = False

    def __str__(self):
        return self.titulo

# DESCRIÇÕES

class Observacao(models.Model):
    id = models.AutoField(primary_key=True)

    servico = models.ForeignKey(
        Servico,
        on_delete=models.DO_NOTHING,
        db_column="servico_id"
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        db_column="usuario_id"
    )

    texto = models.TextField()

    data_registro = models.DateField(
        auto_now_add=False,
        null=True
    )

    class Meta:
        db_table = "observacoes"
        managed = False