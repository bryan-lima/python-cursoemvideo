# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = int(input('Digite um número entre 0 e 9999: '))
unit = num // 1 % 10
ten = num // 10 % 10
hundred = num // 100 % 10
thousand = num // 1000 % 10

print('Unidade: {}' .format(unit))
print('Dezena: {}' .format(ten))
print('Centena: {}' .format(hundred))
print('Milhar: {}' .format(thousand))
