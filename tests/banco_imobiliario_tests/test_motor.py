"""
Testes do módulo de motor
"""
from unittest import TestCase
from banco_imobiliario.tabuleiro import TabuleiroBuilder
from banco_imobiliario.jogador import Jogador
from banco_imobiliario.motor import Motor
from banco_imobiliario import dado
from banco_imobiliario.propriedade import Propriedade
from .jogador_test import JogadorDefinido


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
            .add_jogador(jogador := JogadorDefinido(False), 88, 17, True) \
            .add_propriedade(20, 100, 20) \
            .build()

        dado.viciar([ 4 ])

        motor = Motor(tabuleiro)

        motor.turno()

        self.assertEqual(tabuleiro.jogadores[jogador].saldo, 188)


    def test_pagar_aluguel(self):
        """
        DADO Que o jogador ativo está em seu turno
        QUANDO O jogador ativo cair numa propriedade que já tem dono
        ENTÃO o jogador ativo deve pagar o valor do aluguel ao dono da propriedade
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador_ativo := Jogador(), 100, 5, True) \
            .add_jogador(jogador_dono := Jogador(), 100, 0, False) \
            .add_propriedade(30, 100, 20) \
            .build()

        tabuleiro.propriedades[9].dono = jogador_dono

        motor = Motor(tabuleiro)

        dado.viciar([ 4 ])

        motor.turno()

        self.assertEqual(tabuleiro.jogadores[jogador_ativo].saldo, 70)
        self.assertEqual(tabuleiro.jogadores[jogador_dono].saldo, 130)


    def test_comprar_propriedade(self):
        """
        DADO Que o jogador ativo esteja em seu turno
        QUANDO O jogador ativo cair numa propriedade sem dono
        ENTÃO O jogador ativo poderá comprar a propriedade
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador := JogadorDefinido(True), 100, 5, True) \
            .add_propriedade(30, 80, 20) \
            .build()

        motor = Motor(tabuleiro)

        dado.viciar([ 4 ])

        motor.turno()

        self.assertEqual(tabuleiro.jogadores[jogador].saldo, 20)
        self.assertEqual(tabuleiro.propriedades[9].dono, jogador)



    def test_recusar_comprar_propriedade(self):
        """
        DADO Que o jogador ativo esteja em seu turno
        QUANDO O jogador ativo cair numa propriedade sem dono
        ENTÃO O jogador ativo poderá recusar a comprar a propriedade
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador := JogadorDefinido(False), 100, 5, True) \
            .add_propriedade(30, 80, 20) \
            .build()

        motor = Motor(tabuleiro)

        dado.viciar([ 4 ])

        motor.turno()

        self.assertEqual(tabuleiro.jogadores[jogador].saldo, 100)
        self.assertEqual(tabuleiro.propriedades[9].dono, None)



    def test_comprar_propriedade_sem_saldo(self):
        """
        DADO Que o jogador ativo esteja em seu turno
        QUANDO O jogador ativo cair numa propriedade sem dono,
            tentar comprar a propriedade
            e não tiver saldo suficiente
        ENTÃO O motor não deve oferecer a compra ao jogador
        """

        tabuleiro = TabuleiroBuilder() \
            .add_jogador(jogador := JogadorDefinido(True), 0, 5, True) \
            .add_propriedade(30, 80, 20) \
            .build()

        motor = Motor(tabuleiro)

        dado.viciar([ 4 ])

        motor.turno()

        self.assertEqual(jogador.compra_oferecida, False)
