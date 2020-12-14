# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$ 1,00 = R$ 3,27

wallet = float(input('Quanto dinheiro você tem na carteira? R$ '))
dollarQuote = 3.27
buyDollar = wallet / dollarQuote
print('Com R$ {:.2f} e a cotação do dólar em US$ {}, você pode comprar US$ {:.2f}' .format(wallet, dollarQuote, buyDollar))
