"""
Testes dos agentes
"""
from unittest import TestCase
from banco_imobiliario.motor import Motor
from banco_imobiliario.tabuleiro import TabuleiroBuilder
from banco_imobiliario import dado
from banco_imobiliario.agentes import AgenteImpulsivo, AgenteExigente


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



class AgenteExigenteTestCase(TestCase):
    """
    Testes do agente exigente
    """

    def test_comportameno(self):
        """
        DADO Que o agente seja exigente
        QUANDO Uma compra for oferecida
        ENTÃO O agente deve aceitar a compra apenas se o valor do aluguel for maior do que 50
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador := AgenteExigente(), 200, 0, True) \
            .add_propriedade(20, 100) \
            .add_propriedade(70, 100) \
            .add_propriedade(20, 100) \
            .build()

        dado.viciar([ 1, 1 ])

        motor = Motor(tabuleiro)

        motor.turno()
        motor.turno()

        self.assertEqual(tabuleiro.propriedades[1].dono, jogador)
        self.assertEqual(tabuleiro.propriedades[2].dono, None)
