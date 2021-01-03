# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo de alistamento
# Seu programa também deveria mostrar o tempo que falta ou que passou do prazo

from datetime import date
from sys import exit

yearOfBirth = int(input('Ano de nascimento: '))
currentYear = date.today().year
age = currentYear - yearOfBirth

if age < 0:
    print('Ano de nascimento inválido!')
    exit(0)
elif age == 0 or age == 1:
    print('\nQuem nasceu em {} tem {} ano em {}.' .format(yearOfBirth, age, currentYear))
else:
    print('\nQuem nasceu em {} tem {} anos em {}.' .format(yearOfBirth, age, currentYear))

if age == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif age < 18:
    differenceForEighteen = 18 - age
    enlistmentYear = currentYear + differenceForEighteen
    if differenceForEighteen == 1:
        print('Ainda falta {} ano para o alistamento.' .format(differenceForEighteen))
    else:
        print('Ainda faltam {} anos para o alistamento.' .format(differenceForEighteen))
    print('Seu alistamento será em {}.' .format(enlistmentYear))
elif age > 18:
    differenceForEighteen = age - 18
    enlistmentYear = currentYear - differenceForEighteen
    if differenceForEighteen == 1:
        print('Você já deveria ter se alistado há {} ano.' .format(differenceForEighteen))
    else:
        print('Você já deveria ter se alistado há {} anos.' .format(differenceForEighteen))
    print('Seu alistamento foi em {}.' .format(enlistmentYear))
