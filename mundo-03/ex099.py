# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep


def separator(number):
    print('-=' * number)


def bigger(* numbers):
    separator(30)
    print('Analisando os valores passados...')
    for number in numbers:
        print(f'{number} ', end='')
        sleep(0.3)
    if len(numbers) < 2:
        print(f'→ Foi informado {len(numbers)} valor ao todo.')
    else:
        print(f'→ Foram informados {len(numbers)} valores ao todo.')
    if numbers == ():
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(numbers)}.')


bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger()
