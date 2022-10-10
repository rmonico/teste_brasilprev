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
        Retorna false caso o jogador tenha perdido a partida
        """

        casas = dado.lancar()

        terminou_volta = self.tabuleiro.andar(casas)

        propriedade = self.tabuleiro.propriedades[self.tabuleiro.jogador_ativo_status().posicao]

        status = self.tabuleiro.jogador_ativo_status()

        if propriedade.dono:
            self.tabuleiro.jogadores[propriedade.dono].saldo += propriedade.aluguel
            status.saldo -= propriedade.aluguel

            if status.saldo < 0:
                jogador_ativo = self.tabuleiro.jogador_ativo()
                self.tabuleiro.jogadores.pop(jogador_ativo)
                for propriedade in self.tabuleiro.propriedades:
                    if propriedade.dono == self.tabuleiro.jogador_ativo():
                        propriedade.dono = None

                return False

        else:
            if propriedade.valor <= status.saldo:
                if self.tabuleiro.jogador_ativo().comprar(status, propriedade):
                    status.saldo -= propriedade.valor
                    propriedade.dono = self.tabuleiro.jogador_ativo()

        if terminou_volta:
            self.tabuleiro.jogador_ativo_status().saldo += 100

        return True


    def jogar(self):
        for _ in range(1, 1001):
            for __ in range(len(self.tabuleiro.jogadores)):
                if self.turno():
                    self.tabuleiro.jogador_ativo_idx += 1
                    if self.tabuleiro.jogador_ativo_idx == len(self.tabuleiro.jogadores):
                        self.tabuleiro.jogador_ativo_idx = 0
                else:
                    if len(self.tabuleiro.jogadores) == 1:
                        return list(self.tabuleiro.jogadores.keys())[0]

        return list(self.tabuleiro.jogadores.keys())[0]
