# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação
# Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da Chapecoense

# Tabela Campeonato Brasileiro - Temporada 2020-21
brazilianChampionshipTable = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Palmeiras',
                              'Fluminense', 'Corinthians', 'Santos', 'Ceará SC', 'Atlético-PR', 'Atlético-GO',
                              'Bragantino', 'Sport Recife', 'Vasco da Gama', 'Fortaleza', 'Bahia', 'Goiás',
                              'Botafogo', 'Coritiba')

team = 'Chapecoense'

print('-=' * 21)
print('CAMPEONATO BRASILEIRO | TEMPORADA 2020-21')
print('-=' * 21)
print(f'Lista de times do Brasileirão: {brazilianChampionshipTable}')
print('-=' * 15)
print(f'Os 5 primeiros são {brazilianChampionshipTable[0:5]}')
print('-=' * 15)
print(f'Os últimos 4 são {brazilianChampionshipTable[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(brazilianChampionshipTable)}')
print('-=' * 15)
if team in brazilianChampionshipTable:
    teamPosition = brazilianChampionshipTable.index(team) + 1
    print(f'O {team} está na {teamPosition}ª posição')
else:
    print(f'Infelizmente, o {team} não está na primeira divisão no campeonato desta temporada')
