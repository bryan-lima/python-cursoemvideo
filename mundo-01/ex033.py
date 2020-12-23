# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

# Verifica menor número
smallestNumber = n1
if n2 < n1 and n2 < n3:
    smallestNumber = n2
if n3 < n1 and n3 < n2:
    smallestNumber = n3

# Verifica maior número
higherNumber = n1
if n2 > n1 and n2 > n3:
    higherNumber = n2
if n3 > n1 and n3 > n2:
    higherNumber = n3

print('O MENOR valor digitado foi {}' .format(smallestNumber))
print('O MAIOR valor digitado foi {}' .format(higherNumber))
