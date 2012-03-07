from piston.handler import BaseHandler
from financeiro.empenho.models import Empenho

class EmpenhoHandler(BaseHandler):
    model = Empenho
