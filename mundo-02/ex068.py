# Faça um programa que jogue par ou ímpar com o computador
# O jogo só será interrompido quando o usuário PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

victory = 0

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')

while True:
    # Jogada do computador
    numberRandom = randint(0, 10)

    # Jogada do jogador
    print('=-' * 15)
    chosenNumber = int(input('Diga um número: '))
    chosenOption = ' '
    while chosenOption not in 'PI':
        chosenOption = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    if chosenOption in 'P':
        chosenOption = 'PAR'
    elif chosenOption in 'IÍ':
        chosenOption = 'ÍMPAR'
    print('-' * 30)

    # Verifica se é PAR ou ÍMPAR
    sum = numberRandom + chosenNumber
    if sum % 2 == 0:
        evenOrOdd = 'PAR'
    elif sum % 2 != 0:
        evenOrOdd = 'ÍMPAR'
    print(f'Você jogou {chosenNumber} e o computador jogou {numberRandom}. Total de {sum} deu {evenOrOdd}')
    print('-' * 30)

    # Verifica ganhador
    if chosenOption == evenOrOdd:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        victory += 1
    elif chosenOption != evenOrOdd:
        print('Você PERDEU!')
        break

print('=-' * 15)

print('\nGAME OVER! Você venceu ', end='')
if victory == 0:
    print('nenhuma vez')
elif victory == 1:
    print(f'{victory} vez')
else:
    print(f'{victory} vezes')
