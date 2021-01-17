# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta

# Minha solução inicial
# matrix = [[], [], []]
#
# print()
# for line in range(0, 3):
#     for column in range(0, 3):
#         num = int(input(f'Digite um valor para [{line}, {column}]: '))
#         if line == 0:
#             matrix[0].append(num)
#         elif line == 1:
#             matrix[1].append(num)
#         elif line == 2:
#             matrix[2].append(num)
#
# print('-=' * 30)
# print()
# for column in matrix[0]:
#     print(f'[ {column:^5} ]', end='')
# print()
# for column in matrix[1]:
#     print(f'[ {column:^5} ]', end='')
# print()
# for column in matrix[2]:
#     print(f'[ {column:^5} ]', end='')
# print()

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))

print('-=' * 30)
print()
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}]', end='')
    print()
