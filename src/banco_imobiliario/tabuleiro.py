"""
Módulo de tabuleiro
"""
from .jogador import Jogador
from .propriedade import Propriedade


class TabuleiroBuilder:
    """
    Cria uma instância de Tabuleiro
    """

    def __init__(self):
        self._jogadores = {}
        self._total_propriedades = 0


    def add_jogador(self, jogador: Jogador, saldo: int, posicao: int):
        """
        Adiciona um novo jogador ao jogo
        """
        self._jogadores[jogador] = JogadorStatus(saldo, posicao)

        return self


    def total_propriedades(self, total: int):
        """
        Define o total de propriedades que o tabuleiro terá
        """
        self._total_propriedades = total

        return self


    def build(self):
        """
        Constrói a instância do tabuleiro
        """
        tabuleiro = Tabuleiro()

        for _ in range(self._total_propriedades):
            tabuleiro.propriedades.append(Propriedade())

        for jogador, status in self._jogadores.items():
            tabuleiro.jogadores[jogador] = status

        return tabuleiro


class JogadorStatus:
    """
    Status de um jogador
    """

    def __init__(self, saldo, posicao):
        self.saldo = saldo
        self.posicao = posicao


class Tabuleiro:
    """
    Armazena todo o estado interno do Jogo
    """

    def __init__(self):
        self.jogadores = {}
        self.propriedades = []
        self.jogador_ativo_idx = -1


    def jogador_ativo(self) -> Jogador:
        """
        Devolve o jogador ativo
        """
        return self.jogadores[self.jogador_ativo_idx]


    def andar(self, casas: int) -> bool:
        """
        Anda avança um jogador por um determinado número de casas.
        Retorna True case o jogador tenha completado uma volta.
        """
        # self.posicoes[self.jogador_ativo()] += casas
