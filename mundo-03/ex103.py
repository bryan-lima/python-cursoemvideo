# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def datasheet(name='<desconhecido>', goals=0):
    print(f'O jogador {name} fez {goals} gol(s) no campeonato.')


print('-' * 30)
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    datasheet(goals=g)
else:
    datasheet(n, g)
