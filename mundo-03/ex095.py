# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

team = []
soccerPlayer = {}
goalsList = []

while True:
    soccerPlayer.clear()
    goalsList.clear()

    soccerPlayer['name'] = str(input('\nNome do jogador: ')).strip()
    matches = int(input(f'Quantas partidas {soccerPlayer["name"]} jogou? '))
    for i in range(1, matches + 1):
        goalsList.append(int(input(f'   Quantos gols na partida {i}? ')))
    soccerPlayer['goals'] = goalsList[:]
    soccerPlayer['total'] = sum(goalsList)
    team.append(soccerPlayer.copy())

    while True:
        proceed = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if proceed in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if proceed == 'N':
        break
print('-=' * 30)

print(f'\nCÓD {"NOME":<15} {"GOLS":<15} TOTAL')
print('-' * 42)
for index, player in enumerate(team):
    print(f'{index:>3} ', end='')
    for value in player.values():
        print(f'{str(value):<15}', end=' ')
    print()

while True:
    print('-' * 42)
    choosePlayer = int(input('\nMostrar dados de qual jogador? (999 para parar): '))
    if choosePlayer == 999:
        break
    if choosePlayer >= len(team):
        print(f'ERRO! Não existe jogador com código {choosePlayer}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR: {team[choosePlayer]["name"]}')
        for index, goals in enumerate(team[choosePlayer]['goals']):
            print(f'    No jogo {index + 1} fez {goals} ', end='')
            if goals < 2:
                print('gol.')
            else:
                print('gols.')

print('\n<< VOLTE SEMPRE >>')
