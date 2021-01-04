# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

counter = 0
sum = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        counter += 1
        sum += i

print('\nA soma de todos os {} valores solicitados é {}' .format(counter, sum))
