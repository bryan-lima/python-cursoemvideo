# Crie um programa que vai gerar cinco números aleatórios e colocar em um tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

# Resolução Professor
# from random import randint
# tupleOfNumbers = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

from random import sample
tupleOfNumbers = tuple(sample(range(11), 5))

print(f'Os valores sorteados foram: ', end='')
for i in tupleOfNumbers:
    print(f'{i} ', end='')
print(f'\nO maior valor sorteado foi {max(tupleOfNumbers)}')
print(f'O menor valor sorteado foi {min(tupleOfNumbers)}')
