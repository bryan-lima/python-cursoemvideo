# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" e "F"
# Caso esteja errado, peça a digitação novamente até ter um valor correto

sex = str(input('\nInforme o sexo [M/F]: ')).strip().upper()

while sex not in 'MF':
    sex = str(input('Dados inválidos. Por favor, informe o sexo [M/F]: ')).strip().upper()

print('\nSexo {} registrado com sucesso' .format(sex))
