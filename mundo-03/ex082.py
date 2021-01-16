# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e o valores ímpares digitados, respectivamente
# Ao final, mostre o conteúdo das três listas geradas

listFull = []
listPairs = []
listOdd = []

while True:
    proceed = ' '

    listFull.append(int(input('Digite um número: ')))
    while proceed not in 'SN':
        proceed = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if proceed == 'N':
        break

for number in listFull:
    if number % 2 == 0:
        listPairs.append(number)
    else:
        listOdd.append(number)

print()
print('-=' * 30)
print(f'A lista completa é {listFull}')
print(f'A lista de pares é {listPairs}')
print(f'A lista de ímpares é {listOdd}')
