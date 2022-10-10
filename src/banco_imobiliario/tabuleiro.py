"""
Módulo de tabuleiro
"""
from .jogador import Jogador, JogadorStatus
from .propriedade import Propriedade


class TabuleiroBuilder:
    """
    Cria uma instância de Tabuleiro
    """

    def __init__(self):
        self._jogadores = {}
        self._propriedades = []
        self._jogador_ativo = -1


    def add_jogador(self, jogador: Jogador, saldo: int, posicao: int, ativo: bool = False):
        """
        Adiciona um novo jogador ao jogo
        """
        self._jogadores[jogador] = JogadorStatus(saldo, posicao)

        if ativo:
            self._jogador_ativo = len(self._jogadores) - 1

        return self


    def add_propriedade(self, aluguel: int, valor: int, quantidade: int = 1):
        """
        Cria uma ou mais propriedades com o aluguel específicado
        """
        for _ in range(quantidade):
            self._propriedades.append(Propriedade(aluguel, valor))

        return self


    def build(self):
        """
        Constrói a instância do tabuleiro
        """
        tabuleiro = Tabuleiro()

        tabuleiro.jogador_ativo_idx = self._jogador_ativo

        tabuleiro.propriedades = self._propriedades

        for jogador, status in self._jogadores.items():
            tabuleiro.jogadores[jogador] = status

        return tabuleiro


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
        return list(self.jogadores.keys())[self.jogador_ativo_idx]


    def jogador_ativo_status(self) -> JogadorStatus:
        return self.jogadores[self.jogador_ativo()]


    def andar(self, casas: int) -> bool:
        """
        Anda avança um jogador por um determinado número de casas.
        Retorna True case o jogador tenha completado uma volta.
        """
        assert casas < len(self.propriedades), "Não é permitido andar mais" \
        " casas de uma vez do que a quantidade de propriedades do tabuleiro!"

        self.jogador_ativo_status().posicao += casas

        if self.jogador_ativo_status().posicao < len(self.propriedades):
            return False

        self.jogador_ativo_status().posicao -= len(self.propriedades)

        return True
