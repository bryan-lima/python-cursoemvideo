# Crie um programa que simule o funcionamento de um caixa eletrônico
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

from datetime import datetime

print('=' * 30)
print('{:^30}' .format('BANCO CEV'))
print('=' * 30)

withdrawValue = int(input('Que valor você quer sacar? R$ '))
print('\n', end='')

amount = withdrawValue
banknote = 50
counterBanknote = 0

while True:
    if amount >= banknote:
        amount -= banknote
        counterBanknote += 1
    else:
        if counterBanknote == 1:
            print(f'Total de {counterBanknote} cédula de R$ {banknote}')
        if counterBanknote > 1:
            print(f'Total de {counterBanknote} cédulas de R$ {banknote}')
        if banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1
        counterBanknote = 0
        if amount == 0:
            break

print('\n', end='')
print('=' * 30)
print('Volte sempre ao BANCO CEV! ', end='')

currentTime = int(datetime.now().strftime('%H'))
if (currentTime >= 0) and (currentTime <= 5):
    print('Tenha uma boa madrugada!')
elif (currentTime >= 6) and (currentTime <= 11):
    print('Tenha um bom dia!')
elif (currentTime >= 12) and (currentTime <= 17):
    print('Tenha uma boa tarde!')
elif (currentTime >= 18) and (currentTime <= 23):
    print('Tenha uma boa noite!')
