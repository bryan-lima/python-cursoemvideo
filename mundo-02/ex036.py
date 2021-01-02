# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

colors = {
    'clear': '\033[m',
    'txtRedBold': '\033[1:31m',
    'txtGreenBold': '\033[1:32m',
    'txtYellowBold': '\033[1:33m',
    'txtBlueBold': '\033[1:34m',
}

print('{}====================={}' .format(colors['txtYellowBold'], colors['clear']))
print('{} EMPRÉSTIMO BANCÁRIO{}' .format(colors['txtYellowBold'], colors['clear']))
print('{}====================={}' .format(colors['txtYellowBold'], colors['clear']))

houseValue = float(input('Valor da casa: R$ '))
buyerSalary = float(input('Salário do comprador: R$ '))
financingYears = int(input('Quantos anos de financiamento? '))

print('\n{}Aguarde!{}' .format(colors['txtYellowBold'], colors['clear']))
print('{}Calculando valor da prestação mensal....{}' .format(colors['txtBlueBold'], colors['clear']))
sleep(1)

financingValue = houseValue / (financingYears * 12)
thirtyPercentSalary = (buyerSalary / 100) * 30

print('\nPara pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.' .format(houseValue, financingYears, financingValue))

if financingValue <= thirtyPercentSalary:
    print('\n{}Empréstimo pode ser CONCEDIDO!{}'.format(colors['txtGreenBold'], colors['clear']))
else:
    print('\n{}Empréstimo NEGADO!{}'.format(colors['txtRedBold'], colors['clear']))
