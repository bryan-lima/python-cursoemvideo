# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

numbersPerExtensive = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    print('\n', end='')
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Tente novamente. ', end='')
    print(f'Você digitou o número {numbersPerExtensive[num]}\n')
    proceed = ' '
    while proceed not in 'SN':
        proceed = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if proceed == 'N':
        break

print('\n', end='')
print('{:-^35}' .format(' FIM DO PROGRAMA '))
