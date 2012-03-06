from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=20)

class Pedido(models.Model):
    coordenacao = models.ForeignKey(Setor)

class Empenho(models.Model):
    pedido = models.ForeignKey(Pedido)
