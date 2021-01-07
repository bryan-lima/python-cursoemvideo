# Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

answer = 'S'
sum = counter = numberHigher = numberLower = 0

while answer in 'S':
    n = int(input('\nDigite um número: '))
    sum += n
    counter += 1
    if counter == 1:
        numberHigher = n
        numberLower = n
    else:
        if n > numberHigher:
            numberHigher = n
        elif n < numberLower:
            numberLower = n
    answer = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while answer != 'S' and answer != 'N':
        print('\nOpção inválida! Digite somente [S]im ou [N]ão.')
        answer = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

average = sum / counter

if counter == 1:
    print('\nVocê digitou {} número, e a média é {:.2f}' .format(counter, average))
else:
    print('\nVocê digitou {} números, e a média foi {:.2f}' .format(counter, average))
print('O maior valor foi {} e o menor foi {}' .format(numberHigher, numberLower))
