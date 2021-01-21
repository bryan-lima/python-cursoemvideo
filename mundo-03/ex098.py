# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep


def separator(number):
    print('-=' * number)


def counter(start, stop, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    separator(30)
    print(f'Contagem de {start} até {stop} de {step} em {step}')
    sleep(1)
    if start < stop:
        for i in range(start, stop + 1, step):
            print(f'{i} ', end='')
            sleep(0.5)
    elif stop < start:
        for i in range(start, stop - 1, - step):
            print(f'{i} ', end='')
            sleep(0.5)
    print('→ FIM!')
    sleep(0.5)


counter(1, 10, 1)

counter(10, 0, 2)

print('\nAgora é sua vez de personalizar a contagem!')
init = int(input('Início: '))
end = int(input('Fim: '))
move = int(input('Passo: '))
counter(init, end, move)
