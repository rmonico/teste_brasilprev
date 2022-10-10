"""
Testes dos agentes
"""
from unittest import TestCase
from banco_imobiliario.motor import Motor
from banco_imobiliario.tabuleiro import TabuleiroBuilder
from banco_imobiliario import dado
from banco_imobiliario.agentes import AgenteImpulsivo


class AgenteImpulsivoTestCase(TestCase):
    """
    Testes do agente impulsivo
    """

    def test_comportameno(self):
        """
        DADO Que o agente seja impulsivo
        QUANDO Uma compra for oferecida
        ENTÃO O agente sempre deve aceitar a compra
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador := AgenteImpulsivo(), 100, 0, True) \
            .add_propriedade(20, 100, 20) \
            .build()

        dado.viciar([ 4 ])

        motor = Motor(tabuleiro)

        motor.turno()

        self.assertEqual(tabuleiro.jogadores[jogador].saldo, 0)
        self.assertEqual(tabuleiro.propriedades[4].dono, jogador)
