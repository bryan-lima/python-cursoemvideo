# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

angle = float(input('Digite um ângulo qualquer: '))
print('O ângulo de {} tem o SENO de {:.2f}' .format(angle, sin(radians(angle))))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(angle, cos(radians(angle))))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(angle, tan(radians(angle))))
