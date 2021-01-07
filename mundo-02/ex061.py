# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while

print('\nGerador de PA')
print('-=' * 10)

firstTerm = int(input('\nPrimeiro termo: '))
reason = int(input('Razão: '))
term = firstTerm
counter = 1

while counter <= 10:
    print('{} → ' .format(term), end='')
    term += reason
    counter += 1
print('FIM')
