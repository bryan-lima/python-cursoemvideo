# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno

def area(width, length):
    print(f'A área de um terreno {width}m x {length}m é de {width * length:.1f}m²')


print(' Controle de Terrenos')
print('-' * 22)
w = float(input('LARGURA (m): '))
l = float(input('COMPRIMENTO (m): '))
print()
area(w, l)
