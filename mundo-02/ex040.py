# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

from sys import exit

colors = {
    'clear': '\033[m',
    'txtRedBold': '\033[1:31m',
    'txtGreenBold': '\033[1:32m',
    'txtYellowBold': '\033[1:33m',
}

n1 = float(input('Primeira nota: '))
if n1 < 0 or n1 > 10:
    print('\nNota inválida! Tente novamente.')
    exit(0)
n2 = float(input('Segunda nota: '))
if n2 < 0 or n2 > 10:
    print('\nNota inválida! Tente novamente.')
    exit(0)
average = (n1 + n2) / 2

print('\nTirando {:.1f} e {:.1f}, a média do aluno é {:.1f}' .format(n1, n2, average))
print('O aluno está ', end='')
if average < 5:
    print('{}REPROVADO{}' .format(colors['txtRedBold'], colors['clear']))
elif (average >= 5) and (average < 7):
    print('em {}RECUPERAÇÃO{}' .format(colors['txtYellowBold'], colors['clear']))
elif average >= 7:
    print('{}APROVADO{}' .format(colors['txtGreenBold'], colors['clear']))
