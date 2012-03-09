from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from financeiro.api.handlers import SetorHandler, PedidoHandler, OrcamentoHandler, EmpenhoHandler

setor_resource = Resource(SetorHandler)
pedido_resource = Resource(PedidoHandler)
orcamento_resource = Resource(OrcamentoHandler)
empenho_resource = Resource(EmpenhoHandler)

urlpatterns = patterns('',
   url(r'^pedidos$', pedido_resource),
   url(r'^orcamentos$', orcamento_resource),
   url(r'^empenhos$', empenho_resource),
   url(r'^setores$', setor_resource),
)
