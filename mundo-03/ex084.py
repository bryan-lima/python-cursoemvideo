# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

data = []
people = []

while True:
    proceed = ' '

    data.append(str(input('\nNome: ').strip()))
    data.append(float(input('Peso (kg): ')))
    people.append(data[:])
    data.clear()

    while proceed not in 'SN':
        proceed = str(input('Quer continuar? [S/N]: ').strip().upper())[0]
    if proceed == 'N':
        break

for person in people:
    if people.index(person) == 0:
        weightGreater = person[1]
        weightLower = person[1]
    if person[1] > weightGreater:
        weightGreater = person[1]
    elif person[1] < weightLower:
        weightLower = person[1]

print(f'\nAo todo você cadastrou {len(people)} pessoas.')
print(f'O maior peso foi de {weightGreater:.1f} kg. Peso de ', end='')
for person in people:
    if person[1] == weightGreater:
        print(f'[{person[0]}] ', end='')
print()
print(f'O menor peso foi de {weightLower:.1f} kg. Peso de ', end='')
for person in people:
    if person[1] == weightLower:
        print(f'[{person[0]}] ', end='')
print()
