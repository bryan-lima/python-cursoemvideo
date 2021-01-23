# Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a possibilidade de um número de tipo inválido
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

colors = {
    'clear': '\033[m',
    'txtRedNormal': '\033[0:31m',
    'txtRedBold': '\033[1:31m',
}


def readInt(msg):
    while True:
        try:
            value = int(input(msg))
        except (TypeError, ValueError):
            print(colors['txtRedNormal'] + 'ERRO: Por favor, digite um número inteiro válido.' + colors['clear'])
            continue
        except (KeyboardInterrupt):
            print(colors['txtRedNormal'] + '\nUsuário preferiu não digitar esse número.' + colors['clear'])
            return 0
        else:
            return value


def readFloat(msg):
    while True:
        try:
            value = float(input(msg))
        except (TypeError, ValueError):
            print(colors['txtRedNormal'] + 'ERRO: Por favor, digite um número real válido.' + colors['clear'])
            continue
        except (KeyboardInterrupt):
            print(colors['txtRedNormal'] + '\nUsuário preferiu não digitar esse número.' + colors['clear'])
            return 0
        else:
            return value


numberInt = readInt('Digite um Inteiro: ')
numberFloat = readFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {numberInt} e o real foi {numberFloat}')
