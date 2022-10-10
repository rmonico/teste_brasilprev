"""
Módulo de propriedade
"""


class Propriedade:
    """
    Armazena o estado de uma propriedade
    """

    def __init__(self, aluguel: int, valor: int):
        self.dono = None
        self.aluguel = aluguel
        self.valor = valor
