# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais o aumento é de R$ 15%

currentSalary = float(input('Qual é o salário do funcionário? R$ '))

if currentSalary > 1250:
    percentageIncrease = 10
else:
    percentageIncrease = 15

newSalary = currentSalary + (currentSalary * percentageIncrease / 100)
print('Quem ganhava R$ {:.2f}, com aumento de {}%, passa a ganhar R$ {:.2f} agora' .format(currentSalary, percentageIncrease, newSalary))
