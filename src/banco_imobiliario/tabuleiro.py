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
        self._total_propriedades = -1
        self._jogador_ativo = -1


    def add_jogador(self, jogador: Jogador, saldo: int, posicao: int, ativo: bool = False):
        """
        Adiciona um novo jogador ao jogo
        """
        self._jogadores[jogador] = JogadorStatus(saldo, posicao)

        if ativo:
            self._jogador_ativo = len(self._jogadores) - 1

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
        
        tabuleiro.jogador_ativo_idx = self._jogador_ativo

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
        self._ordem_jogadores = None

    def jogador_ativo(self) -> Jogador:
        if not self._ordem_jogadores:
            self._ordem_jogadores = list(self.jogadores.keys())

        return self._ordem_jogadores[self.jogador_ativo_idx]


    def jogador_ativo_status(self) -> JogadorStatus:
        return self.jogadores[self.jogador_ativo()]


    def andar(self, casas: int) -> bool:
        """
        Anda avança um jogador por um determinado número de casas.
        Retorna True case o jogador tenha completado uma volta.
        """
        self.jogador_ativo_status().posicao += casas

        return False
