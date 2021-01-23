# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from lib.interface import *
from time import sleep

colors = {
    'clear': '\033[m',
    'txtWhiteNormal': '\033[0:30m',
    'txtRedNormal': '\033[0:31m',
    'txtGreenNormal': '\033[0:32m',
    'txtYellowNormal': '\033[0:33m',
    'txtBlueNormal': '\033[0:34m',
    'txtPurpleNormal': '\033[0:35m',
    'txtCyanNormal': '\033[0:36m',
    'txtGrayNormal': '\033[0:37m',
    'txtWhiteBold': '\033[1:30m',
    'txtRedBold': '\033[1:31m',
    'txtGreenBold': '\033[1:32m',
    'txtYellowBold': '\033[1:33m',
    'txtBlueBold': '\033[1:34m',
    'txtPurpleBold': '\033[1:35m',
    'txtCyanBold': '\033[1:36m',
    'txtGrayBold': '\033[1:37m',
}

while True:
    print()
    opt = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if opt == 1:
        print()
        header('Opção 1 selecionada')
    elif opt == 2:
        print()
        header('Opção 2 selecionada')
    elif opt == 3:
        print('\n' + colors["txtRedBold"], end='')
        header('Saindo do sistema... Até logo!')
        print(colors['clear'])
        break
    else:
        print(colors['txtRedBold'] + 'ERRO! Digite uma opção válida!' + colors['clear'])
    sleep(2)
