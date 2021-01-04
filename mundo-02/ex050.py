# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares
# Se o valor digitado for ímpar, desconsidere-o

counter = 0
sum = 0

for i in range(1, 7):
    n = int(input('Digite o {}º valor: ' .format(i)))
    if n % 2 == 0:
        counter += 1
        sum += n

if counter < 2:
    print('\nVocê informou {} número PAR, e a soma foi {}' .format(counter, sum))
else:
    print('\nVocê informou {} números PARES, e a soma foi {}' .format(counter, sum))
