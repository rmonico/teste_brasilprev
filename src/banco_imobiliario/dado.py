"""
Módulo de dado
"""
from random import choice


def lancar() -> int:
    """
    Sorteia um número aleatório entre 1 e 6
    """

    return choice(range(1, 7))
