# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
option = 0

while option != 5:
    print('\n[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    option = int(input("\n>>>>> Qual é a sua opção?: "))
    if option == 1:
        sum = n1 + n2
        print('\nA soma entre {} e {} é {}' .format(n1, n2, sum))
    elif option == 2:
        multiplication = n1 * n2
        print('\nO resultado de {} x {} é {}' .format(n1, n2, multiplication))
    elif option == 3:
        if n1 != n2:
            if n1 > n2:
                numberHigher = n1
            elif n2 > n1:
                numberHigher = n2
            print('\nEntre {} e {} o maior valor é {}' .format(n1, n2, numberHigher))
        elif n1 == n2:
            print('\nEntre {} e {} não há maior valor' .format(n1, n2))
    elif option == 4:
        print('\nInforme os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif option == 5:
        print('\nFinalizando...')
    else:
        print('\nOpção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)

print('Fim do programa! Volte sempre!')
