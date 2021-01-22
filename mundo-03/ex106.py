# Faça um mini-sistema que utilize o Interactive Help do Python
# O usuário vai digitar o comando e o manual vai aparecer
# Quando o usuário digitar a palavra "FIM", o programa se encerrará
# OBS: use cores

from time import sleep

colors = {
    'clear': '\033[m',
    'txtWhiteBoldBgRed': '\033[1;;41m',
    'txtWhiteBoldBgGreen': '\033[1;;42m',
    'txtWhiteBoldBgYellow': '\033[1;;43m',
    'txtWhiteBoldBgBlue': '\033[1;;44m',
    'txtBlackBgWhite': '\033[7;40m',
}


def formatTitle(msg, color):
    tilde = len(msg) + 4
    print(f'{color}', end='')
    print('~' * tilde)
    print(f'  {msg}')
    print('~' * tilde)
    print(colors['clear'], end='')
    sleep(1)


def interactiveHelp(command):
    formatTitle(f'Acessando o manual do comando \'{command}\'', colors['txtWhiteBoldBgBlue'])
    print(colors['txtBlackBgWhite'], end='')
    help(command)
    print(colors['clear'], end='')
    sleep(2)


cmd = ' '
while True:
    formatTitle('SISTEMA DE AJUDA PyHELP', colors['txtWhiteBoldBgGreen'])
    cmd = str(input('Função ou Biblioteca > '))
    if cmd.strip().upper() == 'FIM':
        break
    else:
        interactiveHelp(cmd)
formatTitle('Até logo!', colors['txtWhiteBoldBgRed'])
