# Faça um programa que leia o peso de cinco pessoas
# No final, mostre qual foi o maior e o menor peso lidos

greaterWeight = 0
lowerWeight = 0

for i in range(1, 6):
    weight = float(input('Peso da {}ª pessoa? ' .format(i)))
    if i == 1:
        greaterWeight = weight
        lowerWeight = weight
    if weight > greaterWeight:
        greaterWeight = weight
    if weight < lowerWeight:
        lowerWeight = weight

print('\nO maior peso lido foi de {:.1f}kg' .format(greaterWeight))
print('O menor peso lido foi de {:.1f}kg' .format(lowerWeight))
