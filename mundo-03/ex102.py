# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular,
# e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
# cálculo do fatorial

def factorial(n, show=False):
    """
    # EN-US:
    → Calculates the factorial of a number.
    :param n: The number to be calculated.
    :param show: (Optional) Whether or not to show the account.
    :return: The Factorial value of a number n.

    # PT-BR:
    → Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    print('-' * 30)
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')
    return f


help(factorial)

print(factorial(5, show=True))
print()

print(factorial(5))
print()

fact = int(input('Digite um número para calcular seu fatorial: '))
while True:
    display = str(input('Deseja mostrar a conta? [S/N]: ')).strip().upper()[0]
    if display in 'SN':
        break
if display == 'S':
    display = True
elif display == 'N':
    display = False
print()
print(factorial(fact, display))
