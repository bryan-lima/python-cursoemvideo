# Crie um programa que leia a idade e o sexo de várias pessoas
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos

counterAdult = counterMan = counterWoman = 0

while True:
    sex = ' '
    proceed = ' '

    print('\n', end='')
    print('-' * 30)
    print('{:^30}' .format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    age = int(input('Idade: '))
    if age > 18:
        counterAdult += 1
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sex == 'M':
        counterMan += 1
    if sex == 'F' and age < 20:
        counterWoman += 1
    print('-' * 30)
    while proceed not in 'SN':
        proceed = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if proceed == 'N':
        break

print('\n====== FIM DO PROGRAMA ======')
print(f'\nTotal de pessoas com mais de 18 anos: {counterAdult}')

if counterMan == 0:
    print('Ao todo não há homem cadastrado')
elif counterMan == 1:
    print(f'Ao todo temos {counterMan} homem cadastrado')
else:
    print(f'Ao todo temos {counterMan} homens cadastrados')

if counterWoman == 0:
    print('E não temos mulher com menos de 20 anos')
elif counterWoman == 1:
    print(f'E temos {counterWoman} mulher com menos de 20 anos')
else:
    print(f'E temos {counterWoman} mulheres com menos de 20 anos')
