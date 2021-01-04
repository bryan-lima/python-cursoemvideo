# Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from sys import exit
from datetime import date

currentYear = date.today().year
counterAdult = 0
counterYoung = 0

for i in range(1, 8):
    yearOfBirth = int(input('Em que ano a {}ª pessoa nasceu? ' .format(i)))
    if yearOfBirth > currentYear:
        print('\nAno de nascimento inválido! Tente novamente.')
        exit(0)
    age = currentYear - yearOfBirth
    if age >= 21:
        counterAdult += 1
    else:
        counterYoung += 1

if counterAdult <= 1:
    print('\nAo todo tivemos {} pessoa maior de idade' .format(counterAdult))
else:
    print('\nAo todo tivemos {} pessoas maiores de idade' .format(counterAdult))

if counterYoung <= 1:
    print('E também tivemos {} pessoa menor de idade' .format(counterYoung))
else:
    print('E também tivemos {} pessoas menores de idade' .format(counterYoung))
