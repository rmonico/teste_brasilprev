"""
Módulo de Motor
"""
from .tabuleiro import Tabuleiro
from . import dado


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

        casas = dado.lancar()

        terminou_volta = self.tabuleiro.andar(casas)

        propriedade = self.tabuleiro.propriedades[self.tabuleiro.jogador_ativo_status().posicao]

        if propriedade.dono:
            self.tabuleiro.jogadores[propriedade.dono].saldo += propriedade.aluguel
            self.tabuleiro.jogador_ativo_status().saldo -= propriedade.aluguel
        elif self.tabuleiro.jogador_ativo().comprar(propriedade):
            self.tabuleiro.jogador_ativo_status().saldo -= propriedade.valor
            propriedade.dono = self.tabuleiro.jogador_ativo()

        if terminou_volta:
            self.tabuleiro.jogador_ativo_status().saldo += 100
