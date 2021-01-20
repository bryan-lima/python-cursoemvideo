# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

people = []
person = {}
sumAge = groupMeanAge = 0

while True:
    person['name'] = str(input('\nNome: ')).strip()
    while True:
        person['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if person['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    person['age'] = int(input('Idade: '))
    people.append(person.copy())

    while True:
        proceed = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if proceed in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if proceed == 'N':
        break
print('-=' * 30)

print(f'A) Ao todo temos {len(people)} pessoas cadastradas.')

for person in people:
    sumAge += person['age']
groupMeanAge = sumAge / len(people)
print(f'B) A média de idade é de {groupMeanAge:.2f} anos.')

print(f'C) As mulheres cadastradas foram ', end='')
for person in people:
    if person['sexo'] == 'F':
        print(person['name'], end=" ")
print()

print(f'D) Lista das pessoas que estão com idade acima da média:')
for person in people:
    if person['age'] > groupMeanAge:
        print(f'    nome = {person["name"]}; sexo = {person["sexo"]}; idade = {person["age"]};')

print('\n<< ENCERRADO >>')
