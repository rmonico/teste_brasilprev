"""
Jogadores usados para testes
"""
from banco_imobiliario.jogador import Jogador


class JogadorDefinido(Jogador):

    def __init__(self, comprar: bool):
        self._comprar = comprar


    def comprar(self, propriedade):
        return self._comprar
