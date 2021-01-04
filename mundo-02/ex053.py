# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

phrase = str(input('Digite uma frase: ')).strip().upper()
formattedPhrase = ''.join(phrase.split())
reverse = ''
for i in range(len(formattedPhrase) - 1, -1, -1):
    reverse += formattedPhrase[i]

# Solução mais simples, sem usar o for
# reverse = formattedPhrase[::-1]

print('\nO inverso de {} é {}' .format(formattedPhrase, reverse))
if reverse == formattedPhrase:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
