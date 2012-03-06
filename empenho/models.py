from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=20)


class Pedido(models.Model):
    coordenacao = models.ForeignKey(Setor)
    descricao = models.CharField(max_length=200)


class Orcamento(models.Model):
    pedido = models.ForeignKey(Pedido)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class Empenho(models.Model):
    orcamento = models.ForeignKey(Orcamento)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
