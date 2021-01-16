# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# Caso o número já exista lá dentro, ele não será adicionado
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

listOfNumbers = []

while True:
    proceed = ' '
    num = int(input('\nDigite um valor: '))
    if num not in listOfNumbers:
        listOfNumbers.append(num)
        print(f'Valor adicionado com sucesso...\n')
    else:
        print(f'Valor duplicado! Não vou adicionar...\n')
    while proceed not in 'SN':
        proceed = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if proceed == 'N':
        break

print()
print('-=' * 30)
print(f'Você digitou os valores {sorted(listOfNumbers)}')
