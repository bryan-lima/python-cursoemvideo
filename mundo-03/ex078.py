# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

listOfNumbers = []

print()
for i in range(0, 5):
    listOfNumbers.append(int(input(f'Digite um valor para a posição {i}: ')))

print('=-' * 30)
print()
print(f'Você digitou os valores {listOfNumbers}')

print(f'O maior valor digitado foi {max(listOfNumbers)} ', end='')
if listOfNumbers.count(max(listOfNumbers)) == 1:
    print('na posição ', end='')
else:
    print('nas posições ', end='')
for index, number in enumerate(listOfNumbers):
    if number == max(listOfNumbers):
        print(f'{index}... ', end='')

print(f'\nO menor valor digitado foi {min(listOfNumbers)} ', end='')
if listOfNumbers.count(min(listOfNumbers)) == 1:
    print('na posição ', end='')
else:
    print('nas posições ', end='')
for index, number in enumerate(listOfNumbers):
    if number == min(listOfNumbers):
        print(f'{index}... ', end='')
print()
