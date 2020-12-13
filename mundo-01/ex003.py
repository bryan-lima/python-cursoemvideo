n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
sum = n1 + n2

# Sintaxe utilizada no Python 2
print('A soma entre', n1, 'e', n2, 'vale', sum)

# Sintaxe utilizada no Python 3+
print('A soma entre {} e {} vale {}' .format(n1, n2, sum))
