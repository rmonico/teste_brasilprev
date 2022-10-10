"""
Jogadores usados para testes
"""
from banco_imobiliario.jogador import Jogador


class JogadorDefinido(Jogador):

    def __init__(self, comprar: bool):
        self._comprar = comprar
        self.compra_oferecida = False


    def comprar(self, status, propriedade):
        self.compra_oferecida = True
        return self._comprar
