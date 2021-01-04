# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

colors = {
    'clear': '\033[m',
    'txtRedBold': '\033[1:31m',
    'txtGreenBold': '\033[1:32m',
    'txtYellowBold': '\033[1:33m',
    'txtBlueBold': '\033[1:34m',
}

n = int(input('\nDigite um número inteiro: '))
counter = 0

print('\n', end='')
for i in range(1, n + 1):
    if n % i == 0:
        print('{}' .format(colors['txtBlueBold']), end='')
        counter += 1
    else:
        print('{}' .format(colors['txtRedBold']), end='')
    print('{}{} ' .format(i, colors['clear']), end='')

print('\n\nO número {} foi divisível ' .format(n), end='')
if counter <= 1:
    print('{} vez' .format(counter))
else:
    print('{} vezes'.format(counter))

if counter == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
