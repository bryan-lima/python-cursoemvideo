# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

currentPrice = float(input('Qual é o preço do produto? R$ '))
percentageDiscount = 5
discountPrice = (currentPrice / 100) * (100 - percentageDiscount)
print('O produto que custava R$ {:.2f}, na promoção com desconto de {}% passa a custar R$ {:.2f}' .format(currentPrice, percentageDiscount, discountPrice))
