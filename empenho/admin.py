from django.contrib import admin
from empenho.models import Setor, Pedido, Orcamento, Empenho

admin.site.register(Setor)
admin.site.register(Pedido)
admin.site.register(Orcamento)
admin.site.register(Empenho)
