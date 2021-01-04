# Crie um programa que faça o computador jogar Jokenpô com você

from sys import exit
from time import sleep
from random import randint

options = ('PEDRA', 'PAPEL', 'TESOURA')

# Jogada do computador
numberRandom = randint(0, 2)
computerChoice = options[numberRandom]

# Jogada do jogador
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
numberChoice = int(input('\nQual é a sua jogada? '))
if numberChoice < 0 or numberChoice > 2:
    print('\nJogada inválida! Tente novamente.')
    exit(0)
playerChoice = options[numberChoice]

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\n')

print('-=' * 12)
print('Computador jogou {}' .format(computerChoice))
print('Jogador jogou {}' .format(playerChoice))
print('-=' * 12)

# Verifica ganhador
if computerChoice == playerChoice:
    print('\nEMPATE')
    exit(0)
else:
    if computerChoice == 'PEDRA':
        if playerChoice == 'PAPEL':
            winner = 'JOGADOR'
        elif playerChoice == 'TESOURA':
            winner = 'COMPUTADOR'
    elif computerChoice == 'PAPEL':
        if playerChoice == 'PEDRA':
            winner = 'COMPUTADOR'
        elif playerChoice == 'TESOURA':
            winner = 'JOGADOR'
    elif computerChoice == 'TESOURA':
        if playerChoice == 'PEDRA':
            winner = 'JOGADOR'
        elif playerChoice == 'PAPEL':
            winner = 'COMPUTADOR'
    print('\n{} VENCE' .format(winner))
