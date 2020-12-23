# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite

velocity = float(input('Qual é a velocidade atual do carro? '))

if velocity > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R$ {:.2f}!' .format((velocity - 80) * 7))

print('Tenha um bom dia! Dirija com segurança!')
