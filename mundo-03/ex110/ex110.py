# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui

import currency

price = float(input('Digite o preço: R$ '))
rateOfIncrease = int(input('Digite a taxa de aumento: '))
rateOfDecrease = int(input('Digite a taxa de redução: '))
currency.resume(price, rateOfIncrease, rateOfDecrease)
