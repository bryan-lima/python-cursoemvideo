# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
# No final, mostre a lista ordenada na lista

orderedList = []

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if len(orderedList) == 0 or num > max(orderedList):
        orderedList.append(num)
        print('Adicionado ao final da lista...')
    else:
        for index, number in enumerate(orderedList):
            if num <= number:
                orderedList.insert(index, num)
                print(f'Adicionado na posição {index} da lista')
                break

print()
print('-=' * 30)
print(f'Os valores digitados em ordem foram {orderedList}')
