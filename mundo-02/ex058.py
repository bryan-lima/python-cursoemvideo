# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint

numberRandom = randint(0, 10)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

hit = False
counterHunch = 0

while not hit:
    numberHunch = int(input('\nQual é o seu palpite? '))
    counterHunch += 1
    if numberHunch == numberRandom:
        hit = True
    elif numberHunch < numberRandom:
        print('Mais... Tente mais uma vez.')
    elif numberHunch > numberRandom:
        print('Menos... Tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns!' .format(counterHunch))
