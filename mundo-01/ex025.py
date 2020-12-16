# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

name = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem SILVA? {}' .format('SILVA' in name.upper()))
