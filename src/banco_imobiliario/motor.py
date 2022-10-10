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

        status = self.tabuleiro.jogador_ativo_status()

        if propriedade.dono:
            self.tabuleiro.jogadores[propriedade.dono].saldo += propriedade.aluguel
            status.saldo -= propriedade.aluguel

            perdeu = status.saldo < 0
            if perdeu:
                jogador_ativo = self.tabuleiro.jogador_ativo()
                self.tabuleiro.jogadores.pop(jogador_ativo)
                for propriedade in self.tabuleiro.propriedades:
                    if propriedade.dono == self.tabuleiro.jogador_ativo():
                        propriedade.dono = None

        else:
            if propriedade.valor <= status.saldo:
                if self.tabuleiro.jogador_ativo().comprar(status, propriedade):
                    status.saldo -= propriedade.valor
                    propriedade.dono = self.tabuleiro.jogador_ativo()

        if terminou_volta:
            self.tabuleiro.jogador_ativo_status().saldo += 100
