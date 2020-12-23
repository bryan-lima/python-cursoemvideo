# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

from datetime import date

year = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é BISSEXTO!' .format(year))
else:
    print('O ano {} NÃO é BISSEXTO!' .format(year))
