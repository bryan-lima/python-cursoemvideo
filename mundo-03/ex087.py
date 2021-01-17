# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumOfPairs = sumValuesThirdColumn = 0

for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))

print('-=' * 30)
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}] ', end='')
        if matrix[line][column] % 2 == 0:
            sumOfPairs += matrix[line][column]
        if column == 2:
            sumValuesThirdColumn += matrix[line][column]
    print()

print('-=' * 30)
print(f'A soma dos valores pares é {sumOfPairs}')
print(f'A soma dos valores da terceira coluna é {sumValuesThirdColumn}')
print(f'O maior valor da segunda linha é {max(matrix[1])}')
