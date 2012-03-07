from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from financeiro.api.handlers import EmpenhoHandler

empenho_resource = Resource(EmpenhoHandler)

urlpatterns = patterns('',
   url(r'^empenho/(?P<id>\d+)$', empenho_resource),
   url(r'^empenho$', empenho_resource),
)
