# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa encerra quando ele disse que quer mostrar 0 termos

print('\nGerador de PA')
print('-=' * 10)

firstTerm = int(input('\nPrimeiro termo: '))
reason = int(input('Razão da PA: '))
term = firstTerm
counterTerm = 0
counter = 1
stopFlag = 10

while stopFlag != 0:
    counterTerm += stopFlag
    while counter <= counterTerm:
        print('{} → ' .format(term), end='')
        term += reason
        counter += 1
    print('PAUSA')
    stopFlag = int(input('\nQuantos termos você quer mostrar a mais? '))
print('\nProgressão finalizada com {} termos mostrados.' .format(counterTerm))
