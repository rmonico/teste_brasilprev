# -*- coding: utf-8 -*-
import logging


_logger = logging.getLogger(__name__)


def parse_command_line():
    from argparse import ArgumentParser

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
    args = parse_command_line()

    logging.basicConfig(level=args.logger_level)

    _logger.debug('Root logger configured to level %s', args.logger_level)

    return 0


if __name__ == '__main__':
    returncode = main() or 0

    _logger.warning(f'Exiting with status {returncode}')

    exit(returncode)

