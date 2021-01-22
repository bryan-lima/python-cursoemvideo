# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico

def readInt(msg):
    while True:
        value = str(input(msg))
        if value.isnumeric():
            value = int(value)
            break
        else:
            print('\033[1:31mERRO! Digite um número inteiro válido.\033[m')
    return value


n = readInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
