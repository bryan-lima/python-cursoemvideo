# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

n = float(input('Digite um número real: '))
print('O valor digitado foi {} e a sua parte inteira é igual a {}' .format(n, trunc(n)))
