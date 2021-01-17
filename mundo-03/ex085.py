# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares
# No final, mostre os valores pares e ímpares em ordem crescente

numbers = [[], []]

print()
for i in range(1, 8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)

print('-=' * 30)
print()
print(f'Os valores pares digitados foram: {sorted(numbers[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numbers[1])}')
