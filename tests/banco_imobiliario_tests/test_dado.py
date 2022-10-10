"""
Testes do módulo dado
"""
from unittest import TestCase
from banco_imobiliario import dado


class DadoTestCase(TestCase):
    """
    Testes do módulo dado
    """

    def test_lancar_dado(self):
        """
        QUANDO o dado for lançado
        ENTÃO deve retornar um número inteiro aleatório entre 1 e 6
        """

        for _ in range(10000):
            resultado = dado.lancar()

            self.assertTrue(resultado >= 1)
            self.assertTrue(resultado <= 6)

            # TODO Somar a quantidade de vezes que cada resultado é obtido para verificar se a
            # quantidade de vezes é próximo a 1/6 para cada um
