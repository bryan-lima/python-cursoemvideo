# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

currentSalary = float(input('Qual é o salário do funcionário? R$ '))
percentageIncrease = 15
newSalary = currentSalary + ((currentSalary * percentageIncrease) / 100)
print('O funcionário que ganhava R$ {:.2f}, com o aumento de {}% passa a receber R$ {:.2f}' .format(currentSalary, percentageIncrease, newSalary))
