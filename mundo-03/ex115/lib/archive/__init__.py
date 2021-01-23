from lib.interface import *

def fileExists(file):
    try:
        f = open(file, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(file):
    try:
        f = open(file, 'wt+')
        f.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {file} criado com sucesso!')


def readFile(file):
    try:
        f = open(file, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        header('PESSOAS CADASTRADAS')
        print(f.read())

