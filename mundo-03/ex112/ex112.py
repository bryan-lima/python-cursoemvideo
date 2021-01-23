# Dentro do pacote utilidadesCeV que criamos no DESAFIO 111, temos um módulo chamado dado
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de
# dados para aceitar apenas valores que sejam monetários

from utilitiescev import currency
from utilitiescev import data

price = data.readMoney('Digite o preço: R$ ')
print()
currency.resume(price, 35, 22)
