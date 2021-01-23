# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado
# Transfira todas as funções utilizadas nos DESAFIOS 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando

from utilitiescev import currency

price = float(input('Digite o preço: R$ '))
rateOfIncrease = int(input('Digite a taxa de aumento: '))
rateOfDecrease = int(input('Digite a taxa de redução: '))
currency.resume(price, rateOfIncrease, rateOfDecrease)
