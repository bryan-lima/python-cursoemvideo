# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

from random import randint
from time import sleep


def sortition(listOfNumbers):
    print(f'\nSorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        random = randint(1, 10)
        listOfNumbers.append(random)
        print(f'{random} ', end='')
        sleep(0.3)
    print('→ PRONTO!')


def sumPair(listOfNumbers):
    summation = 0
    for number in listOfNumbers:
        if number % 2 == 0:
            summation += number
    print(f'\nSomando os valores pares de {numbers}, temos {summation}')


numbers = []
sortition(numbers)
sumPair(numbers)
