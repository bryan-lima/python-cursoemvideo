# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

city = str(input('Em que cidade você nasceu? ')).strip()
print('A cidade começa com o nome SANTO? {}' .format('SANTO' in city.upper().split()[0]))
