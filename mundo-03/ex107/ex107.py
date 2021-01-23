# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()
# Faça também um programa que importe esse módulo e use algumas dessas funções

from currency import increase, double, half

price = float(input('\nDigite o preço: R$ '))

print(f'A metade de R$ {price} é R$ {half(price)}')
print(f'O dobro de R$ {price} é R$ {double(price)}')
print(f'Aumentando 10%, temos R$ {increase(price, 10)}')
