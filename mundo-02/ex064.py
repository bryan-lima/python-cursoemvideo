# Crie um programa que leia vários números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

n = sum = counter = 0

while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        sum += n
        counter += 1

if counter == 0:
    print('\nVocê não digitou um número')
elif counter == 1:
    print('\nVocê digitou {} número e a soma entre ele é {}' .format(counter, sum))
else:
    print('\nVocê digitou {} números e a soma entre eles foi {}' .format(counter, sum))
