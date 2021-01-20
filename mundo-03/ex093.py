# Crie um programa que gerencie o aproveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidas ele jogou
# Depois vai ler a quantidade de gols feitos em cada partida
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

soccerPlayer = {}
goalsList = []

soccerPlayer['name'] = str(input('Nome do jogador: ')).strip()
matches = int(input(f'Quantas partidas {soccerPlayer["name"]} jogou? '))
for i in range(0, matches):
    goalsList.append(int(input(f'   Quantos gols na partida {i}? ')))
soccerPlayer['goals'] = goalsList[:]
soccerPlayer['total'] = sum(goalsList)
print('-=' * 30)

print(soccerPlayer)
print('-=' * 30)

for k, v in soccerPlayer.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {soccerPlayer["name"]} jogou {len(soccerPlayer["goals"])} partidas')
for index, value in enumerate(soccerPlayer["goals"]):
    print(f'    => Na partida {index}, fez {value} ', end='')
    if value < 2:
        print('gol')
    else:
        print('gols')
print(f'Foi um total de {soccerPlayer["total"]} ', end='')
if soccerPlayer["total"] < 2:
    print('gol')
else:
    print('gols')
