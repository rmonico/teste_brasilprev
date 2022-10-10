"""
Módulo de jogador
"""
from .propriedade import Propriedade


class JogadorStatus:
    """
    Status de um jogador
    """

    def __init__(self, saldo, posicao):
        self.saldo = saldo
        self.posicao = posicao


class Jogador:
    """
    Apenas um modelo para a classe de jogador
    """

    def comprar(self, status: JogadorStatus, propriedade: Propriedade) -> bool:
        raise Exception('Não implementado')
