"""
Módulo de jogador
"""
from .propriedade import Propriedade


class Jogador:
    """
    Apenas um modelo para a classe de jogador
    """

    def comprar(self, propriedade: Propriedade) -> bool:
        raise Exception('Não implementado')
