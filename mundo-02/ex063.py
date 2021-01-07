# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

print('-' * 30)
print('{:^30}' .format('Sequência de Fibonacci'))
print('-' * 30)

numberOfTerms = int(input('\nQuantos termos você quer mostrar? '))

termPrevious = 0
termCurrent = 0
termNext = 1
counter = 2

print('~' * 30)
print('0 → ', end='')

while counter <= numberOfTerms:
    print('{} → ' .format(termNext), end='')
    termPrevious = termCurrent
    termCurrent = termNext
    termNext = termPrevious + termCurrent
    counter += 1
print('FIM')
print('~' * 30)
