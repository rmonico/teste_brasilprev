"""
Módulo principal
"""
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import logging
import sys
from .motor import Motor
from .tabuleiro import TabuleiroBuilder
from .agentes import AgenteImpulsivo, AgenteExigente, AgenteCauteloso, AgenteAleatorio


_logger = logging.getLogger(__name__)


def parse_command_line():
    """
    Apenas faz o parse da linha de comando
    """

    parser = ArgumentParser(description='Jogo de banco imobiliário')

    parser.add_argument('--verbosity',
                        '-v',
                        metavar='LEVEL',
                        dest='logger_level',
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'],
                        default='NOTSET',
                        help='Verbosidade do logger')

    return parser.parse_args()


def main():
    """
    Método executado quando o programa é chamado pela linha de comando
    """
    args = parse_command_line()

    logging.basicConfig(level=args.logger_level)

    _logger.debug('Root logger configured to level %s', args.logger_level)


    tabuleiro = TabuleiroBuilder() \
        .add_jogador(AgenteImpulsivo(), 300, 0, True) \
        .add_jogador(AgenteExigente(), 300, 0, False) \
        .add_jogador(AgenteCauteloso(), 300, 0, False) \
        .add_jogador(AgenteAleatorio(), 300, 0, False) \
        .add_propriedade(20, 90, 20) \
        .build()

    motor = Motor(tabuleiro)

    vencedor = motor.jogar()

    print(f'Vencedor: {vencedor.nome}')

    return 0


if __name__ == '__main__':
    STATUS = main() or 0

    _logger.warning('Exiting with status %s', STATUS)

    sys.exit(STATUS)
