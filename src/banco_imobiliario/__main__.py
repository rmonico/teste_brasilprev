"""
Módulo principal
"""
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import logging
import sys


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

    return 0


if __name__ == '__main__':
    STATUS = main() or 0

    _logger.warning('Exiting with status %s', STATUS)

    sys.exit(STATUS)
