"""
Módulo de agentes
"""
from .jogador import Jogador


class AgenteImpulsivo(Jogador):
    """
    O jogador *impulsivo* compra qualquer propriedade sobre a qual ele parar.
    """

    def comprar(self, status, propriedade):
        return True


class AgenteExigente(Jogador):
    """
    O jogador *exigente* compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
    """

    def comprar(self, status, propriedade):
        return propriedade.aluguel > 50


class AgenteCauteloso(Jogador):
    """
    O jogador *cauteloso* compra qualquer propriedade desde que ele tenha uma reserva de 80
    de saldo sobrando depois de realizada a compra.
    """

    def comprar(self, status, propriedade):
        return status.saldo >= propriedade.valor + 80
