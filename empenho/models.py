# -*- coding: utf-8 -*-

from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nome


class Pedido(models.Model):
    coordenacao = models.ForeignKey(Setor)
    descricao = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descricao


class Orcamento(models.Model):
    pedido = models.ForeignKey(Pedido)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '%s (%s)'%(self.pedido.descricao,self.valor_total)


class Empenho(models.Model):
    orcamento = models.ForeignKey(Orcamento)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.orcamento,self.valor
