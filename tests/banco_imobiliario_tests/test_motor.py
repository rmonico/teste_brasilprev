"""
Testes do módulo de motor
"""
from unittest import TestCase
from banco_imobiliario.tabuleiro import TabuleiroBuilder
from banco_imobiliario.jogador import Jogador
from banco_imobiliario.motor import Motor
from banco_imobiliario import dado


class MotorTestCase(TestCase):
    """
    Testes da classede motor
    """

    def test_completar_volta(self):
        """
        DADO que o jogador ativo completou uma volta
        ENTÃO o jogador deve receber 100 de saldo
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador := Jogador(), 88, 17, True) \
            .total_propriedades(20) \
            .build()

        dado.viciar([ 4 ])

        motor = Motor(tabuleiro)

        motor.turno()

        self.assertEqual(tabuleiro.jogadores[jogador].saldo, 188)
