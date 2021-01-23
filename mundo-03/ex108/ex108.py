# Adapte o código do DESAFIO 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado

import currency

price = float(input('\nDigite o preço: R$ '))


print(f'A metade de {currency.currency(price)} é {currency.currency(currency.half(price))}')
print(f'O dobro de {currency.currency(price)} é {currency.currency(currency.double(price))}')
print(f'Aumentando 10%, temos {currency.currency(currency.increase(price, 10))}')
