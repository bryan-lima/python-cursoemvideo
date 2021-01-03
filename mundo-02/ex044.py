# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

from sys import exit

colors = {
    'clear': '\033[m',
    'txtRedBold': '\033[1:31m',
    'txtYellowBold': '\033[1:33m',
    'txtBlueBold': '\033[1:34m',
}

print('{}' .format(colors['txtYellowBold']) + '{:=^40}' .format(' LOJAS LIMA ') + '{}' .format(colors['clear']) + '\n')

purchasePrice = float(input('Preço das compras: R$ '))

print('\n{}' .format(colors['txtBlueBold']) + '{:^30}' .format('FORMAS DE PAGAMENTO:') + '{}' .format(colors['clear']))
print('[1] À vista no dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')

paymentMethod = int(input('\nEscolha uma opção: '))

if paymentMethod == 1:
    discountRate = 10
    finalPrice = purchasePrice - (purchasePrice / 100 * discountRate)
    print('\nCom o pagamento à vista no dinheiro/cheque, ganhou {}% de desconto' .format(discountRate), end='')
elif paymentMethod == 2:
    discountRate = 5
    finalPrice = purchasePrice - (purchasePrice / 100 * discountRate)
    print('\nCom o pagamento à vista no cartão, ganhou {}% de desconto' .format(discountRate), end='')
elif paymentMethod == 3:
    finalPrice = purchasePrice
    parcelQuantity = 2
    parcelValue = finalPrice / parcelQuantity
    print('\nSua compra será parcelada em {}x de R$ {:.2f} SEM JUROS' .format(parcelQuantity, parcelValue), end='')
elif paymentMethod == 4:
    increaseRate = 20
    finalPrice = purchasePrice + (purchasePrice / 100 * increaseRate)
    parcelQuantity = int(input('\nQuantas parcelas? '))
    parcelValue = finalPrice / parcelQuantity
    print('\nSua compra será parcelada em {}x de R$ {:.2f} COM JUROS' .format(parcelQuantity, parcelValue), end='')
else:
    print('\n{}Opção de pagamento inválida! Tente novamente.{}' .format(colors['txtRedBold'], colors['clear']))
    exit(0)
print('\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final' .format(purchasePrice, finalPrice))
