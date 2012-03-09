from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from financeiro.api.handlers import PedidoHandler, OrcamentoHandler, EmpenhoHandler

pedido_resource = Resource(PedidoHandler)
orcamento_resource = Resource(OrcamentoHandler)
empenho_resource = Resource(EmpenhoHandler)

urlpatterns = patterns('',
   url(r'^pedidos$', pedido_resource),
   url(r'^orcamento$', orcamento_resource),
   url(r'^empenhos$', empenho_resource),
)
