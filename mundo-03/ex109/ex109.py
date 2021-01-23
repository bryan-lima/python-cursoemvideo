# Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no DESAFIO 108

import currency

price = float(input('\nDigite o preço: R$ '))


print(f'A metade de {currency.currency(price)} é {currency.half(price, formatted=True)}')
print(f'O dobro de {currency.currency(price)} é {currency.double(price, True)}')
print(f'Aumentando 10%, temos {currency.increase(price, 10, formatted=True)}')
print(f'Reduzindo 13%, temos {currency.decrease(price, 13, True)}')
