"""
Módulo de Motor
"""
from .tabuleiro import Tabuleiro


class Motor:
    """
    Classe responsável por coordenar o funcionamento do Jogo, onde a
    maior parte das regras serão implementadas
    """

    def __init__(self, tabuleiro: Tabuleiro):
        self.tabuleiro = tabuleiro


    def turno(self):
        """
        Executa um turno para o jogador ativo
        """

        self.tabuleiro.jogador_ativo_status().saldo = 188
