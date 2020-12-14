# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros

n = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a:' .format(n))
print('{}km (quilômetros' .format(n / 1000))
print('{}hm (hectômetros' .format(n / 100))
print('{}dam (decâmetros' .format(n / 10))
print('{}dm (decímetros' .format(n * 10))
print('{}cm (centímetros)' .format(n * 100))
print('{}mm (milímetros)' .format(n * 1000))
