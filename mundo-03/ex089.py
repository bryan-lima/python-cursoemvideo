# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

studentReport = []

while True:
    proceed = ' '

    name = str(input('\nNome: ').strip())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    average = (n1 + n2) / 2
    studentReport.append([name, [n1, n2], average])

    while proceed not in 'SN':
        proceed = str(input('Quer continuar? [S/N]: ').strip().upper())
    if proceed == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4} {"NOME":<15} {"MÉDIA":>8}')
print('-' * 30)
for student in studentReport:
    print(f'{studentReport.index(student):<4} {student[0]:<15} {student[2]:>8.1f}')

print('-' * 35)
while True:
    indexStudent = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if indexStudent == 999:
        break
    if indexStudent <= len(studentReport) - 1:
        print(f'Notas de {studentReport[indexStudent][0]} são {studentReport[indexStudent][1]}')
    else:
        print(f'Não existe cadastro de aluno para No. {indexStudent}. Tente novamente.')
    print('-' * 35)

print()
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
