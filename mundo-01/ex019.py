# Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

student1 = input('Nome do primeiro aluno: ')
student2 = input('Nome do segundo aluno: ')
student3 = input('Nome do terceiro aluno: ')
student4 = input('Nome do quarto aluno: ')
students = [student1, student2, student3, student4]
chosenStudent = choice(students)
print('O aluno escolhido foi {}' .format(chosenStudent))
