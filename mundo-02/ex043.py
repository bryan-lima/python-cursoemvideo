# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

weight = float(input('Qual é o seu peso? (Kg) '))
height = float(input('Qual é a sua altura? (m) '))

imc = weight / (height ** 2)
print('\nO IMC dessa pessoa é de {:.1f}' .format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal')
elif (imc >= 18.5) and (imc < 25):
    print('PARABÉNS, você está na faixa de PESO IDEAL')
elif (imc >= 25) and (imc < 30):
    print('Você está em SOBREPESO')
elif (imc >= 30) and (imc < 40):
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
