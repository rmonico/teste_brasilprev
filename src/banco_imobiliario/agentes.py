"""
Módulo de agentes
"""
from .jogador import Jogador


class AgenteImpulsivo(Jogador):

    def comprar(self, propriedade):
        return True
