# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa

from math import hypot

oppositeSide = float(input('Comprimento do cateto oposto: '))
adjacentSide = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa é igual a {:.2f}' .format(hypot(oppositeSide, adjacentSide)))
