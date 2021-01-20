# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
# No final, mostre o conteúdo da estrutura na tela

student = {}
student['name'] = str(input('\nNome: ')).strip()
student['average'] = float(input(f'Média de {student["name"]}: '))

if student['average'] >= 7:
    student['situation'] = 'Aprovado'
elif 5 <= student['average'] < 7:
    student['situation'] = 'Recuperação'
else:
    student['situation'] = 'Reprovado'

print()
print(f'- Nome é igual a {student["name"]}')
print(f'- Média é igual a {student["average"]:.1f}')
print(f'- Situação é igual a {student["situation"]}')
