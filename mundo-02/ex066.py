# Crie um programa que leia vários números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada
# No final , mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

sum = counter = 0

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    sum += n
    counter += 1

print(f'\nA soma dos {counter} valores foi {sum}!')
