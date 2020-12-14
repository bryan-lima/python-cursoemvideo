# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

student1 = input('Nome do primeiro aluno: ')
student2 = input('Nome do segundo aluno: ')
student3 = input('Nome do terceiro aluno: ')
student4 = input('Nome do quarto aluno: ')
students = [student1, student2, student3, student4]
shuffle(students)
print('\nA ordem de apresentação dos alunos será:')
print(students)
