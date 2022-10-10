"""
Módulo de agentes
"""
from .jogador import Jogador
import random


class AgenteImpulsivo(Jogador):
    """
    O jogador *impulsivo* compra qualquer propriedade sobre a qual ele parar.
    """

    def __init__(self):
        self.nome = 'Impulsivo'


    def comprar(self, status, propriedade):
        return True


class AgenteExigente(Jogador):
    """
    O jogador *exigente* compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
    """

    def __init__(self):
        self.nome = 'Exigente'


    def comprar(self, status, propriedade):
        return propriedade.aluguel > 50


class AgenteCauteloso(Jogador):
    """
    O jogador *cauteloso* compra qualquer propriedade desde que ele tenha uma reserva de 80
    de saldo sobrando depois de realizada a compra.
    """

    def __init__(self):
        self.nome = 'Cauteloso'


    def comprar(self, status, propriedade):
        return status.saldo >= propriedade.valor + 80


class AgenteAleatorio(Jogador):
    """
    O jogador *aleatório* compra a propriedade que ele parar em cima com probabilidade de 50%.
    """

    def __init__(self):
        self.nome = 'Aleatório'


    def comprar(self, status, propriedade):
        return random.getrandbits(1) == 1
