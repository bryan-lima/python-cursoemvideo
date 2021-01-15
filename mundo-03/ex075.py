# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em  uma tupla
# No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

tupleOfNumbers = (int(input('Digite um número: ')),
                  int(input('Digite outro número: ')),
                  int(input('Digite mais um número: ')),
                  int(input('Digite o último número: ')))

counterPairs = 0

print(f'\nVocê digitou os valores {tupleOfNumbers}')

if 9 not in tupleOfNumbers:
    print('O valor 9 apareceu nenhuma vez')
elif tupleOfNumbers.count(9) == 1:
    print(f'O valor 9 apareceu {tupleOfNumbers.count(9)} vez')
else:
    print(f'O valor 9 apareceu {tupleOfNumbers.count(9)} vezes')

if 3 in tupleOfNumbers:
    print(f'O valor 3 apareceu na {tupleOfNumbers.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em qualquer posição')

for i in tupleOfNumbers:
    if i % 2 == 0:
        counterPairs += 1

if counterPairs > 0:
    print(f'Os valores pares digitados foram ', end='')
    for i in tupleOfNumbers:
        if i % 2 == 0:
            print(i, end=' ')
else:
    print('Não foi digitado qualquer valor par')
