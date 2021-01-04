# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

from sys import exit

counterAge = 0
olderManAge = 0
counterWoman = 0

for i in range(1, 5):
    print('\n----- {}ª PESSOA -----' .format(i))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()

    counterAge += age

    if sex != 'M' and sex != 'F':
        print('\nSexo informado é inválido! Tente novamente.')
        exit(0)

    if sex == 'M':
        if age > olderManAge:
            olderManAge = age
            olderManName = name

    if sex == 'F':
        if age < 20:
            counterWoman += 1

averageAge = counterAge / 4

print('\nA média de idade do grupo é de {} anos' .format(averageAge))

if olderManAge == 0:
    print('Não há homem no grupo informado')
else:
    print('O homem mais velho tem {} anos e se chama {}' .format(olderManAge, olderManName))

if counterWoman == 0:
    print('Não há mulher com menos de 20 anos' .format(counterWoman))
elif counterWoman == 1:
    print('Ao todo há {} mulher com menos de 20 anos' .format(counterWoman))
else:
    print('Ao todo há {} mulheres com menos de 20 anos' .format(counterWoman))
