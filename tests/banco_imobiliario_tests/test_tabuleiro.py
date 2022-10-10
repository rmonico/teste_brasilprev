"""
Testes do módulo da tabuleiro
"""
from unittest import TestCase
from banco_imobiliario.tabuleiro import TabuleiroBuilder
from banco_imobiliario.jogador import Jogador


class TabuleiroTestCase(TestCase):
    """
    Testes da classe Tabuleiro
    """

    def test_andar(self):
        """
        DADO que há jogador ativo
        QUANDO for solicitado que o jogador ativo ande N casas
        DEVE a posição do jogador ativo deve avançar N casas a frente
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador := Jogador(), 0, 4, True) \
            .total_propriedades(20) \
            .build()

        tabuleiro.andar(3)

        self.assertEqual(tabuleiro.jogadores[jogador].posicao, 7)
