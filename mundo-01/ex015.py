# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

rentedDays = int(input('Quantos dias alugados?: '))
kmRun = float(input('Quantos km rodados?: '))
dailyRent = 60
valueKm = 0.15
payable = (rentedDays * dailyRent) + (kmRun * valueKm)
print('O total a pagar é de R$ {:.2f}' .format(payable))
