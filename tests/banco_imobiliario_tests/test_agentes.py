"""
Testes dos agentes
"""
from unittest import TestCase
from banco_imobiliario.motor import Motor
from banco_imobiliario.tabuleiro import TabuleiroBuilder
from banco_imobiliario import dado
from banco_imobiliario.agentes import AgenteImpulsivo, AgenteExigente, AgenteCauteloso, AgenteAleatorio


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



class AgenteCautelosoTestCase(TestCase):
    """
    Testes do agente cauteloso
    """

    def test_comportameno(self):
        """
        DADO Que o agente seja cauteloso
        QUANDO Uma compra for oferecida
        ENTÃO O agente deve aceitar a compra apenas se após a compra sobrar uma reserva de 80 de saldo
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador := AgenteCauteloso(), 180, 0, True) \
            .add_propriedade(20, 0) \
            .add_propriedade(20, 100) \
            .add_propriedade(20, 10) \
            .build()

        dado.viciar([ 1, 1 ])

        motor = Motor(tabuleiro)

        motor.turno()
        motor.turno()

        self.assertEqual(tabuleiro.propriedades[1].dono, jogador)
        self.assertEqual(tabuleiro.propriedades[2].dono, None)



class AgenteAleatorioTestCase(TestCase):
    """
    Testes do agente aleatório
    """

    def test_comportameno(self):
        """
        DADO Que o agente seja aleatório
        QUANDO Uma compra for oferecida
        ENTÃO O agente deve aceitar a compra de forma aleatória em 50% dos casos
        """

        resultados = {
            True: 0,
            False: 0
        }

        agente = AgenteAleatorio()

        for _ in range(10000):
            resultados[agente.comprar(None, None)] += 1


        # 4750 = (10000 / 2) - 5%
        self.assertGreaterEqual(resultados[True], 4750)

        # 5250 = (10000 / 2) + 5%
        self.assertLessEqual(resultados[True], 5250)

        self.assertGreaterEqual(resultados[False], 4750)
        self.assertLessEqual(resultados[False], 5250)
