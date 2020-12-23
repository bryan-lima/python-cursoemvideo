# Desenvolva um programa que pergunte a distância de uma viagem em km
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas

distance = float(input('Qual é a distância da sua viagem? '))
print('Voê está prestes a começar uma viagem de {}km' .format(distance))

# IF ELSE padrão
if distance <= 200:
    travelFee = 0.5
else:
    travelFee = 0.45

# IF ELSE simplificado ("ternário")
travelFee = 0.5 if distance <= 200 else 0.45

print('E o preço da sua passagem será de R$ {:.2f}' .format(distance * travelFee))
