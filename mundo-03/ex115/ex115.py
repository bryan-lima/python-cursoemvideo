# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from lib.interface import *
from lib.archive import *
from time import sleep

colors = {
    'clear': '\033[m',
    'txtRedNormal': '\033[0:31m',
    'txtGreenNormal': '\033[0:32m',
    'txtYellowNormal': '\033[0:33m',
    'txtBlueNormal': '\033[0:34m',
    'txtRedBold': '\033[1:31m',
    'txtGreenBold': '\033[1:32m',
    'txtYellowBold': '\033[1:33m',
    'txtBlueBold': '\033[1:34m',
}

archive = 'cursoemvideo.txt'

if not fileExists(archive):
    createFile(archive)

while True:
    print()
    opt = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if opt == 1:
        print()
        readFile(archive)
    elif opt == 2:
        print()
        header('NOVO CADASTRO')
        namePerson = str(input('Nome: '))
        agePerson = readInt('Idade: ')
        register(archive, namePerson, agePerson)
    elif opt == 3:
        print('\n' + colors["txtRedBold"], end='')
        header('Saindo do sistema... Até logo!')
        print(colors['clear'])
        break
    else:
        print(colors['txtRedBold'] + 'ERRO! Digite uma opção válida!' + colors['clear'])
    sleep(2)
