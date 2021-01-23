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
        for line in f:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos')
    finally:
        f.close()


def register(file, name='Desconhecido', age=0):
    try:
        f = open(file, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            f.write(f'{name};{age}\n')
        except:
            print('Houve um erro ao gravar dados!')
        else:
            print(f'Novo registro de {name} adicionado.')
            f.close()
