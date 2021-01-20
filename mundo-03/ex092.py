# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário,
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

worker = {}

worker['name'] = str(input('Nome: ')).strip()
yearOfBirth = int(input('Ano de nascimento: '))
worker['age'] = datetime.now().year - yearOfBirth
worker['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if worker['ctps'] != 0:
    worker['yearOfHiring'] = int(input('Ano de contratação: '))
    worker['salary'] = float(input('Salário: R$ '))
    worker['retirement'] = ((worker['yearOfHiring'] + 35) - datetime.now().year) + worker['age']
print('-=' * 30)

for k, v in worker.items():
    print(f'O campo {k} tem valor {v}')
