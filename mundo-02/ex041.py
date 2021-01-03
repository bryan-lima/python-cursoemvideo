# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER

from sys import exit
from datetime import date

yearOfBirth = int(input('Ano de nascimento: '))
currentYear = date.today().year
age = currentYear - yearOfBirth

if yearOfBirth > currentYear:
    print('Ano de nascimento inválido!')
    exit(0)

print('\nO atleta tem {} ' .format(age), end='')
if age == 0 or age == 1:
    print('ano.')
else:
    print('anos.')

print('Classificação: ', end='')
if age <= 9:
    print('MIRIM.')
elif age <= 14:
    print('INFANTIL.')
elif age <= 19:
    print('JÚNIOR.')
elif age <= 25:
    print('SÊNIOR.')
elif age > 25:
    print('MASTER.')
