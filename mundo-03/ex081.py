# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista

listOfNumbers = list()

while True:
    proceed = ' '

    listOfNumbers.append(int(input('Digite um valor: ')))
    while proceed not in 'SN':
        proceed = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if proceed == 'N':
        break

print()
print('-=' * 30)
print(f'Você digitou {len(listOfNumbers)} elementos')
print(f'Os valores em ordem decrescente são {sorted(listOfNumbers, reverse=True)}')
if 5 in listOfNumbers:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
