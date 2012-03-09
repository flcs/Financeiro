from piston.handler import BaseHandler
from financeiro.empenho.models import Setor, Pedido, Orcamento, Empenho


class PedidoHandler(BaseHandler):

    allowed_methods = ("POST")
    model = Pedido

    def create(self, request, *args, **kwargs):
        coordenacao = Setor.objects.get(pk=request.POST.get('coordenacao'))
        novo_pedido = self.model(coordenacao=coordenacao, descricao=request.POST.get('descricao'))
        novo_pedido.save()
        return "Criado\n"

class OrcamentoHandler(BaseHandler):

    allowed_methods = ("POST")
    model = Orcamento

    def create(self, request, *args, **kwargs):
        pedido = Pedido.objects.get(pk=request.POST.get('pedido'))
        novo_orcamento = self.model(pedido=pedido, valor_total=request.POST.get('valor_total'))
        novo_orcamento.save()
        return "Criado\n"


class EmpenhoHandler(BaseHandler):

    allowed_methods = ("POST")
    model = Empenho

    def create(self, request, *args, **kwargs):
        orcamento = Orcamento.objects.get(pk=request.POST.get('orcamento'))
        novo_empenho = self.model(orcamento=orcamento, valor=request.POST.get('valor_total'))
        novo_empenho.save()
        return "Criado\n"
