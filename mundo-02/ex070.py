# Crie um programa que leia o nome e o preço de vários produtos
# O programa deverá perguntar se o usuário vai continuar
# No final, mostre:
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$ 1000
# C) Qual é o nome do produto mais barato

colors = {
    'clear': '\033[m',
    'txtGreenNormal': '\033[0:32m',
    'txtBlueNormal': '\033[0:34m',
    'txtYellowBold': '\033[1:33m',
}

print('{}' .format(colors['txtYellowBold']))
print('-' * 40)
print('{:^40}' .format('LOJA SUPER BARATÃO'))
print('-' * 40)
print('{}' .format(colors['clear']))

purchaseSum = counterProducts = counterProductsOverThousand = 0
productNameCheapest = ' '

while True:
    proceed = ' '

    productName = str(input('Nome do Produto: ')).strip()
    price = float(input('Preço: R$ '))
    counterProducts += 1
    purchaseSum += price

    if counterProducts == 1 or price < priceLowest:
        priceLowest = price
        productNameCheapest = productName

    if price > 1000:
        counterProductsOverThousand += 1

    while proceed not in 'SN':
        proceed = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if proceed == 'N':
        break

    print('-' * 36)

print('{}' .format(colors['txtYellowBold']))
print('{:-^40}' .format(' FIM DO PROGRAMA '))
print('{}' .format(colors['clear']))

print(f'O total da compra foi {colors.get("txtGreenNormal")}R$ {purchaseSum:.2f}{colors.get("clear")}')

if counterProductsOverThousand == 0:
    print('Não há produto custando mais de R$ 1000.00')
elif counterProductsOverThousand == 1:
    print(f'Temos {counterProductsOverThousand} produto custando mais de R$ 1000.00')
else:
    print(f'Temos {counterProductsOverThousand} produtos custando mais de R$ 1000.00')

print(f'O produto mais barato foi {colors.get("txtBlueNormal")}{productNameCheapest}{colors.get("clear")} que custa R$ {priceLowest:.2f}')
