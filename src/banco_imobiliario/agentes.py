"""
Módulo de agentes
"""
from .jogador import Jogador


class AgenteImpulsivo(Jogador):
    """
    O jogador *impulsivo* compra qualquer propriedade sobre a qual ele parar.
    """

    def comprar(self, propriedade):
        return True


class AgenteExigente(Jogador):
    """
    O jogador *exigente* compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
    """

    def comprar(self, propriedade):
        return propriedade.aluguel > 50
