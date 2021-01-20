# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios
# Guarde esses resultados em um dicionário
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

# Solução do professor
# from random import randint
# from time import sleep
# from operator import itemgetter
#
# plays = {'jogador1': randint(1, 6),
#          'jogador2': randint(1, 6),
#          'jogador3': randint(1, 6),
#          'jogador4': randint(1, 6)}
#
# ranking = []
#
# print('Valores sorteados:')
# for key, value in plays.items():
#     print(f'O {key} tirou {value} no dado')
#     sleep(1)
#
# ranking = sorted(plays.items(), key=itemgetter(1), reverse=True)
#
# print()
# print('== RANKING DOS JOGADORES ==')
# for index, tuple in enumerate(ranking):
#     print(f'  {index + 1}º lugar: {tuple[0]} com {tuple[1]}')

from random import randint
from time import sleep
from operator import itemgetter

plays = {}
counter = 0

for i in range(1, 5):
    shot = randint(1, 6)
    plays[f'jogador{i}'] = shot

print('Valores sorteados:')
for key, value in plays.items():
    print(f'O {key} tirou {value} no dado')
    sleep(1)

print()
print('== RANKING DOS JOGADORES ==')
for key, value in sorted(plays.items(), key=itemgetter(1), reverse=True):
    counter += 1
    print(f' {counter}º lugar: {key} com {value}')
