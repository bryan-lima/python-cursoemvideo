# Faça um programa que leia um número qualquer e mostre o seu fatorial

number = int(input('Digite um número para calcular seu fatorial: '))

counter = number
factorial = 1

print('\nCalculando {}! = ' .format(number), end='')
while counter > 0:
    print('{}' .format(counter), end='')
    print(' x ' if counter > 1 else ' = ', end='')
    factorial *= counter
    counter -= 1
print('{}' .format(factorial))
