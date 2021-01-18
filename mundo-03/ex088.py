# Faça um programa que ajude um jogador da MEGA SENA a criar palpites
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

# Resolução proposta pelo professor
# from random import randint
# from time import sleep
#
# list = []
# games = []
# print('-' * 30)
# print(f'{"JOGA NA MEGA SENA":^30}')
# print('-' * 30)
# quantity = int(input('Quantos jogos você quer que eu sorteie? '))
# total = 1
# while total <= quantity:
#     counter = 0
#     while True:
#         num = randint(1, 60)
#         if num not in list:
#             list.append(num)
#             counter += 1
#         if counter >= 6:
#             break
#     list.sort()
#     games.append(list[:])
#     list.clear()
#     total += 1
# print('-=' * 4, f' SORTEANDO {quantity} JOGOS ', '-=' * 4)
# for i, l in enumerate(games):
#     print(f'Jogo {i + 1}: {l}')
#     sleep(1)
# print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)

from time import sleep
from random import sample

numbersMegaSena = []
gamesMegaSena = []

for number in range(1, 61):
    numbersMegaSena.append(number)

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

quantityGames = int(input('Quantos jogos você quer que eu sorteie? '))

print()
print('-=' * 4, f' SORTEANDO {quantityGames:2} JOGOS ', '-=' * 4)

for i in range(1, quantityGames + 1):
    gamesMegaSena.append(sample(numbersMegaSena, 6))
    print(f'Jogo {i}: {sorted(gamesMegaSena[i - 1])}')
    sleep(1)

print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
