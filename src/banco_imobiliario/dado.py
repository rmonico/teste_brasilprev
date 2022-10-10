"""
Módulo de dado
"""
from random import choice


def aleatorio():
    """
    Implementação padrão de resultados
    """
    while True:
        yield choice(range(1, 7))


def viciar(valores: list):
    def resultado_viciado():
        for valor in valores:
            yield valor

    global resultados
    resultados = resultado_viciado()


resultados = aleatorio()


def lancar() -> int:
    """
    Sorteia um número aleatório entre 1 e 6
    """

    return next(resultados)
