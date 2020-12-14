# Faça um programa que leia a largura e a altura de uma parede e metros
# Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

wallHeight = float(input('Altura da parede (em metros): '))
wallWidth = float(input('Largura da parede (em metros): '))
wallArea = wallHeight * wallWidth
inkQuantity = 0.5 * wallArea
print('A parede tem a dimensão de {}x{} e sua área é de {}m²' .format(wallHeight, wallWidth, wallArea))
print('Para pintar essa parede, você precisará de {}l de tinta' .format(inkQuantity))
